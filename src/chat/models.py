from sqlalchemy import Column, Integer, String

from src.db import Base


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    message = Column(String)

    class Meta:
        orm_mode = True

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
