from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True)

    creator_id = Column(Integer, ForeignKey('users.id'))
    opponent_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship('User', back_populates='created_games')
    opponent = relationship('User', back_populates='joined_games')

    turns = relationship('GameTurns', back_populates='game')

    started_at = Column(DateTime)
    finished_at = Column(DateTime)
