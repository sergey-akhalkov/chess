from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from db import Base


class GameTurnModel(Base):
    __tablename__ = 'game_turns'

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    game_id = Column(Integer, ForeignKey('games.id'))

    user = relationship('UserModel', foreign_keys=[user_id])
    game = relationship('GameModel',  foreign_keys=[game_id])

    made_at = Column(DateTime, default=datetime.utcnow)
