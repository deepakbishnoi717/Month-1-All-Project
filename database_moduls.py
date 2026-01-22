from sqlalchemy import Column, Integer , String, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class product(Base):

    __tablename__ = "products"


    id = Column(Integer, primary_key=True ,index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

class bishnoi(Base):
    __tablename__ = "bishnoi"

    name = Column(String, primary_key=True,index = True)
    rule = Column(Integer,default=29,nullable=False)
    cast = Column(String,default = "Bishnoi")
    guru = Column(String, default = "Guru Jambeshwer.")
    place = Column(String, default = "Mukti Dham Mukam.") 

class Data(Base):
    __tablename__ = "data"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    age = Column(Integer)