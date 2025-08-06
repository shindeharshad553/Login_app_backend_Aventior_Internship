from .database import Base
from sqlalchemy import Column,Integer,String

# craeting the models that is the python classes that will be mapped to the database tables
class User(Base):
    __tablename__="LoginData"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(30),unique=True,nullable=False)
    password=Column(String(1000),nullable=False)