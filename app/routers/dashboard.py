
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User

router = APIRouter(prefix="/api/v1/dashboard", tags=["Dashboard"])


@router.get("/{user_id}")
async def student_dashboard(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(User).where(User.id == user_id)
    )

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="Please complete 2FA verification first"
        )

    return {
        "message": f"Welcome {user.full_name}!",
        "user_id": user.id,
        "account_status": "Active",
        "redirect_url": "/dashboard/student"
    }
