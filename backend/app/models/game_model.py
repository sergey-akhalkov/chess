from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from db import Base


class GameModel(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True)

    creator_id = Column(Integer, ForeignKey('users.id'))
    opponent_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship('UserModel', foreign_keys=[creator_id])
    opponent = relationship('UserModel', foreign_keys=[opponent_id])

    started_at = Column(DateTime, default=datetime.utcnow)
    finished_at = Column(DateTime)
