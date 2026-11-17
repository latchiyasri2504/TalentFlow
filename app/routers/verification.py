
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.models.otp import OTPChallenge
from app.schemas.auth import VerifyOTPRequest
from app.services.otp_service import generate_otp, hash_otp, get_expiry_time
from app.services.otp_delivery import send_otp

router = APIRouter(prefix="/api/v1/auth", tags=["Verification"])


@router.post("/send-otp")
async def send_verification_otp(
    email: str,
    channel: str = "email",
    db: AsyncSession = Depends(get_db)
):
    if channel not in ["email", "whatsapp", "browser"]:
        raise HTTPException(status_code=400, detail="Invalid channel")

    result = await db.execute(
        select(User).where(User.email == email)
    )
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.is_active:
        raise HTTPException(status_code=400, detail="Account already verified")

    otp = generate_otp()

    challenge = OTPChallenge(
        user_id=user.id,
        channel=channel,
        otp_hash=hash_otp(otp),
        expires_at=get_expiry_time(),
        is_used=False
    )

    db.add(challenge)
    await db.commit()

    send_otp(channel, email, otp)

    return {"message": f"Development OTP generated for {channel}"}


@router.post("/verify-2fa")
async def verify_otp_code(
    data: VerifyOTPRequest,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(User).where(User.email == data.email)
    )
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    result = await db.execute(
        select(OTPChallenge)
        .where(
            OTPChallenge.user_id == user.id,
            OTPChallenge.channel == data.channel,
            OTPChallenge.is_used == False
        )
        .order_by(OTPChallenge.id.desc())
    )

    challenge = result.scalars().first()

    if not challenge:
        raise HTTPException(status_code=400, detail="OTP not found")

    if challenge.expires_at <= datetime.now(timezone.utc):
        raise HTTPException(status_code=400, detail="OTP expired")

    from app.services.otp_service import verify_otp

    if not verify_otp(data.otp, challenge.otp_hash):
        raise HTTPException(status_code=400, detail="Invalid OTP")

    challenge.is_used = True
    user.is_active = True
    await db.commit()

    from app.services.token import create_access_token

    token = create_access_token(user.id)

    return {
        "message": "Account verified successfully",
        "access_token": token,
        "token_type": "bearer",
        "dashboard": "/dashboard/student"
    }
