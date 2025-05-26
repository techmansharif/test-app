from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import quizzes
from pydantic import BaseModel

app = FastAPI()

# Allow frontend (React) running on localhost:3000 to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(quizzes.router)
