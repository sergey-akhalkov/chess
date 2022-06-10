from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import settings


Base = declarative_base()
async_engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True)
async_session: AsyncSession = sessionmaker(
    async_engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
        await session.commit()
