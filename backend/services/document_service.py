import os
import shutil

from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from fastapi import BackgroundTasks
from tasks.embedding_task import process_document

from models import Document
import os
from fastapi.responses import FileResponse

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def upload_document(title, category, file: UploadFile, current_user, db: Session):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document = Document(
        title=title,
        category=category,
        filename=file.filename,
        filepath=filepath,
        uploaded_by=current_user.id

    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return {
        "message": "Document uploaded successfully",
        "document_id": document.id
    }

from models import Document


def get_all_documents(db: Session):
    documents = db.query(Document).all()

    return documents

def delete_document(document_id: int, db: Session):

    document = db.query(Document).filter(
        Document.id == document_id
    ).first()

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    if os.path.exists(document.filepath):
        os.remove(document.filepath)

    db.delete(document)
    db.commit()

    return {
        "message": "Document deleted successfully"
    }
def download_document(
    document_id: int,
    db: Session
):

    document = db.query(Document).filter(
        Document.id == document_id
    ).first()

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return FileResponse(
        path=document.filepath,
        filename=document.filename,
        media_type="application/pdf"
    )