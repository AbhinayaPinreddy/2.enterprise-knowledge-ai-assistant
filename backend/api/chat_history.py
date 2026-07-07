from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from utils.auth import get_current_user

from schemas import (
    ChatSessionCreate,
    ChatSessionResponse,
    ChatMessageResponse
)

from services.chat_service import (
    create_session,
    get_sessions,
    get_messages
)

router = APIRouter(
    prefix="/chat-history",
    tags=["Chat History"]
)

@router.post(
    "/session",
    response_model=ChatSessionResponse
)
def create_new_session(
    session: ChatSessionCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return create_session(
        session.title,
        current_user.id,
        db
    )

@router.get(
    "/sessions",
    response_model=List[ChatSessionResponse]
)
def get_all_sessions(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_sessions(
        current_user.id,
        db
    )

@router.get(
    "/messages/{session_id}",
    response_model=List[ChatMessageResponse]
)
def get_chat_messages(
    session_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return get_messages(
        session_id,
        db
    )