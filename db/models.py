from sqlalchemy import (Column, String, Integer, ForeignKey, DateTime, Text)
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    manufactured = Column(Integer, nullable=False)
    color = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    reg_date = Column(DateTime, default=datetime.now())


class CarPhoto(Base):
    __tablename__ = "cars_photos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey("cars.id"))
    photo_file = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())

    cars_fk = relationship(Car, lazy='subquery')
