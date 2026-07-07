from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Document, DocumentChunk, ChatSession

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/stats")
def dashboard_stats(db: Session = Depends(get_db)):

    documents = db.query(Document).count()

    chats = db.query(ChatSession).count()

    chunks = db.query(DocumentChunk).count()

    categories = db.query(Document.category).distinct().count()

    recent_documents = (
        db.query(Document)
        .order_by(Document.id.desc())
        .limit(5)
        .all()
    )

    return {
        "documents": documents,
        "chat_sessions": chats,
        "chunks": chunks,
        "categories": categories,
        "recent_documents": [
            {
                "id": doc.id,
                "filename": doc.filename,
                "category": doc.category
            }
            for doc in recent_documents
        ]
    }