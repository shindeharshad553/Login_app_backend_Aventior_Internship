from fastapi import APIRouter,Depends
# Update the import path if login_schemas.py is in the same directory as hello.py
from app.schemas.login_schemas import LoginRequest
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.hashing import Hash



router=APIRouter(
    tags=['register']
)



@router.post("/register")
def register(request: LoginRequest, db: Session = Depends(get_db)):
    hashedPassword = Hash.bcrypt(request.password)
    # let's create a new user in the database
    new_user = models.User(username=request.username, password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user    
    
