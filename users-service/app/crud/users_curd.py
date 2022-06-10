from app.models.user_model import UserModel
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_by_id(db: AsyncSession, user_id: int) -> UserModel:
    query = select(UserModel).where(UserModel.id == user_id)
    results = await db.execute(query)
    return results.scalar_one_or_none()


async def get_by_email(db: AsyncSession, email: str) -> UserModel:
    query = select(UserModel).where(UserModel.email == email)
    results = await db.execute(query)
    return results.scalar_one_or_none()


async def create(db: AsyncSession, user: UserModel) -> int:
    db.add(user)
    await db.commit()
    return user.id
