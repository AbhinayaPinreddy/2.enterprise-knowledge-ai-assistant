from fastapi import APIRouter, UploadFile, File, Form, Depends,BackgroundTasks
from sqlalchemy.orm import Session

from database import get_db
from utils.auth import admin_required
from services.document_service import upload_document,get_all_documents,delete_document,download_document
from typing import List
from schemas import DocumentList
from tasks.embedding_task import process_document_task

from utils.auth import (
    admin_required,
    get_current_user
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/upload")
def upload(
    background_tasks: BackgroundTasks,
    title: str = Form(...),
    category: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    result = upload_document(
        title,
        category,
        file,
        current_user,
        db
    )

    background_tasks.add_task(
        process_document_task,
        result["document_id"]
    )

    return result

@router.get("/", response_model=List[DocumentList])
def get_documents(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_all_documents(db)

@router.delete("/{document_id}")
def delete(
    document_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(admin_required)
):
    return delete_document(
        document_id,
        db
    )
@router.get("/download/{document_id}")
def download(
    document_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return download_document(
        document_id,
        db
    )