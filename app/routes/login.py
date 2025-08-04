from fastapi import APIRouter
# Update the import path if login_schemas.py is in the same directory as hello.py
from app.schemas.login_schemas import LoginRequest


router=APIRouter()

@router.get("/hello",tags=["General"])
def hello():
    return{"hello":"world"}


@router.post("/login",tags=["Login"])
def login(request:LoginRequest):
    if not request:
        raise HTTPException(status_code=401,details="Invalid Login Credentials")
    return {"username": request.username, "password": request.password}
    
