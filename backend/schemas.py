from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class DocumentResponse(BaseModel):
    id: int
    title: str
    category: str
    filename: str
    filepath: str

    class Config:
        from_attributes = True

class DocumentList(BaseModel):
    id: int
    title: str
    category: str
    filename: str
    upload_time: datetime

    class Config:
        from_attributes = True

from pydantic import BaseModel


class ChatSessionCreate(BaseModel):
    title: str


class ChatSessionResponse(BaseModel):

    id: int

    title: str

    class Config:
        from_attributes = True


class ChatMessageResponse(BaseModel):

    id: int

    role: str

    message: str

    class Config:
        from_attributes = True

class ChatRequest(BaseModel):
    session_id: int
    question: str


class ChatResponse(BaseModel):
    answer: str
    sources: list