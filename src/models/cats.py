from sqlalchemy import Column, Integer, Text, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from src.database import Base


class Cat(Base):
    __tablename__ = 'cats'

    cat_id = Column(Integer, autoincrement=True, primary_key=True)
    color = Column(String(length=64), nullable=True)
    age_in_month = Column(Integer, nullable=True)
    description = Column(Text)
    breed_id = Column(ForeignKey('breeds.breed_id'))
    breed: Mapped['Breed'] = relationship('Breed', back_populates='cats')
