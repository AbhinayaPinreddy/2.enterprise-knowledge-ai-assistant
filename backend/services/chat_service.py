from models import ChatSession
from sqlalchemy.orm import Session


def create_session(title, user_id, db):

    session = ChatSession(

        title=title,

        user_id=user_id

    )

    db.add(session)

    db.commit()

    db.refresh(session)

    return session

from models import ChatMessage


def save_message(

    session_id,

    role,

    message,

    db

):

    msg = ChatMessage(

        session_id=session_id,

        role=role,

        message=message

    )

    db.add(msg)

    db.commit()

def get_sessions(

    user_id,

    db

):

    return db.query(

        ChatSession

    ).filter(

        ChatSession.user_id == user_id

    ).all()

def get_messages(

    session_id,

    db

):

    return db.query(

        ChatMessage

    ).filter(

        ChatMessage.session_id == session_id

    ).order_by(

        ChatMessage.created_at

    ).all()