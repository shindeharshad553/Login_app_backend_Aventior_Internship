# this file contains the code to handle the protected routes 

from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError,ExpiredSignatureError
from app.JWTtokens import SECRET_KEY, ALGORITHM
from app.schemas.token_schemas import TokenData
# from login fastapi fetch the token 
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

# get the current active user
def get_current_user(token:str=Depends(oauth2_scheme)):
    print("Token inside get_current_user  ",token)
    credentials_exception=HTTPException(status_code=401,detail="could not validate the credentials",headers={"WWW-Authenticate":"Bearer"})
    # decoded_unverified = jwt.decode(
    #     token,
    #     SECRET_KEY,
    #     algorithms=[ALGORITHM],
    #     options={"verify_signature": False, "verify_exp": False}
    # )

    # print("Unverified claims:", decoded_unverified)
    try:
    
        print(jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM]))
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except ExpiredSignatureError:
        # Specific case: token expired → triggers frontend refresh logic
        raise HTTPException(
            status_code=401,
            detail="Access token expired",
            headers={"WWW-Authenticate": "Bearer"}
        )
    except JWTError:
        # Any other JWT-related error
        raise credentials_exception
    return TokenData(username=username)