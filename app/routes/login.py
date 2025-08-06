from fastapi import APIRouter,Depends
# Update the import path if login_schemas.py is in the same directory as hello.py
from app.schemas.login_schemas import LoginRequest
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from passlib.context import CryptContext # used for password hashing 



router=APIRouter(
    tags=['login']
)

pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")

@router.post("/login")
def login(request:LoginRequest,db:Session=Depends(get_db)):
    hashedPassword=pwd_cxt.hash(request.password)
    # let's create a new user in the database
    new_user=models.User(username=request.username,password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user    
    
