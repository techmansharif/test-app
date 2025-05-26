from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import quizzes
from pydantic import BaseModel
import uvicorn
import os 


app = FastAPI()

# Allow frontend (React) running on localhost:3000 to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",
                   "https://test-deployment-e19fb.web.app",
                   "https://test-deployment-e19fb.firebaseapp.com"],  
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(quizzes.router)


if __name__ == "__main__":
    # Use the PORT environment variable provided by Cloud Run, default to 8000
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
