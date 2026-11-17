
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.database import get_db
from app.models.user import User
from app.schemas.auth import RegisterRequest
from app.services.security import hash_password

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])


@router.post("/register")
async def register(
    data: RegisterRequest,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(User).where(User.email == data.email)
    )

    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        full_name=data.full_name,
        email=data.email,
        phone=data.phone,
        hashed_password=hash_password(data.password),
        is_active=False
    )

    db.add(user)
    print("REGISTER: Before commit")
    await db.commit()
    print("REGISTER: After commit")
    await db.refresh(user)

    return {
        "message": "Registration successful. Account pending verification.",
        "user_id": user.id
    }
