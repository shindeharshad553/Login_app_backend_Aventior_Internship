from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

# create the database URL
SQLCLCHEMY_DATABASE_URL="mysql+mysqlconnector://root:root@localhost:3306/AventiorIntershipLoginData"
engine =create_engine(SQLCLCHEMY_DATABASE_URL)

# create a session local class
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

# function that will be used to get the database session
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()  
    
Base=declarative_base()