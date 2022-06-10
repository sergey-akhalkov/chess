from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
