from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app import JWTtokens
from app.schemas.token_schemas import RefreshRequest
from app.database import get_db
from app import models

router = APIRouter()


# # request to validate the refresh token and return a new access token 
# @router.post("/refresh")
# def refresh(req:RefreshRequest):
#     print(req.refresh_token)
#     payload=JWTtokens.verify_refresh_token(req.refresh_token)
#     print(payload)
#     if payload is None:
#         return {"details":"Invalid refresh token"}
#     # if the refresh token is valid then generate a new access token 
#     username=payload.get("sub")
#     new_access_token=JWTtokens.create_access_token({"sub":username})
#     return {"access_token":new_access_token}


@router.post("/refresh")
def refresh(refresh_token:str,db:Session=Depends(get_db)):
    refresh_token = refresh_token.strip().replace('"', '')
    # look for the refresh token in the database
    db_token=db.query(models.Token).filter(models.Token.refresh_token==refresh_token).first()
    print("db_token",db_token)
    if not db_token:
        print("Token is not found in database")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid refresh token")
    # if refresh token is present and matches then verify the token 
    payload=JWTtokens.verify_refresh_token(refresh_token)
    if payload is None:
        print("payload is none")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid refresh token")
    username :str=payload.get("sub") # type: ignore
    if username is None:
        print("username is none")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid refresh token")
    # create a new acces token 
    new_access_token=JWTtokens.create_access_token({"sub":username})
    
    # update the access token in the database
    db_token.access_token=new_access_token  # type: ignore
    db.commit()
    
    return{
        "access_token":new_access_token,
        "token_type":"bearer"
    }
    