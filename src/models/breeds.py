from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship, Mapped

from src.database import Base
from src.models.cats import Cat


class Breed(Base):
    __tablename__ = 'breeds'

    breed_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(length=64), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    cats: Mapped[list['Cat']] = relationship('Cat', back_populates='breed')
