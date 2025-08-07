from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import register,login,home
from . import models
from .database import engine
from .database import Base



app=FastAPI()

# CORS settings so that the frontend can access the backend 
app.add_middleware(
    CORSMiddleware, #allows cross-origin requests
    allow_origins=["http://localhost:3000"],#allows all origins that you specified in the list to access the API's
    allow_credentials=True,#allows swnding cookies and authentication tokens 
    allow_methods=["*"], #allows all HTTP methods 
    allow_headers=["*"],#allows all customs headers and you want to send JSON and tokens in the headers 

)

app.include_router(register.router)
app.include_router(login.router)
app.include_router(home.router)
# to configure the database and to create the tables
models.Base.metadata.create_all(engine)