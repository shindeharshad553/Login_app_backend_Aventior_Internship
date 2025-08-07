# This is the home route file for the FastAPI application. that are protected by OAuth2 authentication.

from fastapi import APIRouter ,Depends
from app.oauth2 import get_current_user


router=APIRouter()


@router.get("/home")
def home(get_current_user:str=Depends(get_current_user)):
    return {"detail":"We are at home page"}