from fastapi import FastAPI

from database import Base
from database import engine

import models
from api.auth import router as auth_router
from api.documents import router as document_router
from api.chat import router as chat_router
from api.chat_history import router as chat_history_router
from fastapi.middleware.cors import CORSMiddleware
from api.dashboard import router as dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Enterprise Knowledge Assistant"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(document_router)
app.include_router(chat_router)
app.include_router(chat_history_router)
app.include_router(dashboard_router)


@app.get("/")
def home():
    return {
        "message": "Backend is running successfully!"
    }