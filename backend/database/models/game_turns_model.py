from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from database import Base


class GameTurn(Base):
    __tablename__ = 'game_turns'

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')

    game_id = Column(Integer, ForeignKey('game.id'))
    game = relationship('Game', back_populates='turns')

    made_at = Column(DateTime)
