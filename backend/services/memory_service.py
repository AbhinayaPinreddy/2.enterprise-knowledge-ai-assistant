from sqlalchemy.orm import Session
from models import ChatMessage


def load_memory(session_id: int, db: Session, limit: int = 5):

    messages = (
        db.query(ChatMessage)
        .filter(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.created_at.desc())
        .limit(limit)
        .all()
    )

    messages.reverse()

    return messages


def build_conversation(messages):

    conversation = ""

    for msg in messages:

        if msg.role == "user":
            conversation += f"User: {msg.message}\n"

        else:
            conversation += f"Assistant: {msg.message}\n"

    return conversation