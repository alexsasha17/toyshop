from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    
    name = Column(String, unique=True, nullable=False)
    mark = Column(String)
    price = Column(Integer)
    speed = Column(Integer)


class Toy(Base):
    __tablename__ = "toys"

    id = Column(Integer, primary_key=True)
    
    name = Column(String)
    mark = Column(String)
    price = Column(Integer)
