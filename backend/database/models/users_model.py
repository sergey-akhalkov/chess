from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    created_games = relationship('Game', back_populates='creator')
    joined_games = relationship('Game', back_populates='opponent')

    registered_at = Column(DateTime)
