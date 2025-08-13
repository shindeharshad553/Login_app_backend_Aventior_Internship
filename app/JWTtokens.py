# File that is used to store JWT token related constants


from datetime import datetime,timedelta,timezone
from jose import jwt
from jose import JWTError,ExpiredSignatureError

# details for the access token 
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

# details for the refresh token 
REFRESH_SECRET_KEY= "b1c2d3e4f5g6h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x3y4z5a6b7c8d9e0f1g2"
REFRESH_TOKEN_EXPIRE_DAYS=7


# create the access token

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



# create a refresh token 

def create_refresh_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,REFRESH_SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt
    
    
    
# function to verify the refresh token 
def verify_refresh_token(refresh_token:str):
    refresh_token = refresh_token.strip().replace('"', '')
    print("inside refresh token ",refresh_token)
    try:
        payload=jwt.decode(refresh_token,REFRESH_SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        print("Refresh token expired")
    except JWTError as e:
        print("JWT error ",e)
    return None
    