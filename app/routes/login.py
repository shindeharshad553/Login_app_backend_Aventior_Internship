from fastapi import APIRouter,Depends,HTTPException,status 
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.login_schemas import LoginRequest
from sqlalchemy.orm import Session
from app.database import get_db  
from app import models
from app.hashing import Hash
from datetime import timedelta
from app import JWTtokens
from app.schemas import token_schemas
router=APIRouter(
    tags=['login']
)


@router.post("/login")
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    # check whether user exists with the given credentials
    user = db.query(models.User).filter(models.User.username == request.username).first() 
    # if user does not exist, raise an excepption
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid creadentials")
    # Checks the password 
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    # if user exists and password matches then return the JWT token 
    
    access_token = JWTtokens.create_access_token(data={"sub": user.username})
    return token_schemas.Token(access_token=access_token, token_type="bearer")