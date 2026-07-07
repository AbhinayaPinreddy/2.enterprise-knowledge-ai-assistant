from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

from utils.auth import get_current_user

from schemas import ChatRequest

from services.multi_agent_service import ask_question

from services.chat_service import save_message

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    # Save user message
    save_message(
        session_id=request.session_id,
        role="user",
        message=request.question,
        db=db
    )

    # Get AI response
    result = ask_question(
        question=request.question,
        session_id=request.session_id,
        db=db
    )

    # Save assistant message
    save_message(
        session_id=request.session_id,
        role="assistant",
        message=result["answer"],
        db=db
    )

    return result