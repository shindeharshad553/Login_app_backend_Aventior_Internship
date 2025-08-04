from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import login


app=FastAPI()

# CORS settings so that the frontend can access the backend 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(login.router)