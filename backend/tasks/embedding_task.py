from database import SessionLocal
from models import Document, DocumentChunk

from rag.document_processor import process_document
from rag.vector_store import VectorStore


def process_document_task(document_id: int):

    db = SessionLocal()

    try:

        document = db.query(Document).filter(
            Document.id == document_id
        ).first()

        if not document:
            return

        # Update status
        document.embedding_status = "Processing"
        db.commit()

        # Process PDF
        processed_chunks = process_document(
            document.filepath,
            document.id
        )

        # Load existing FAISS index
        store = VectorStore()

        # Number of vectors already in FAISS
        start_index = store.current_size()

        # Add new vectors
        store.add_documents(processed_chunks)

        # Save FAISS index
        store.save()

        # Store chunk metadata in PostgreSQL
        for i, chunk in enumerate(processed_chunks):

            db_chunk = DocumentChunk(
                document_id=chunk["document_id"],
                chunk_index=chunk["chunk_id"],
                faiss_index=start_index + i,
                page=chunk["page"],
                text=chunk["text"]
            )

            db.add(db_chunk)

        db.commit()

        # Update status
        document.embedding_status = "Completed"
        db.commit()

        print("=" * 60)
        print("Embedding Completed")
        print(f"Document : {document.filename}")
        print(f"Chunks   : {len(processed_chunks)}")
        print("=" * 60)

    except Exception as e:

        db.rollback()

        if document:
            document.embedding_status = "Failed"
            db.commit()

        print("Embedding Error:", e)

    finally:

        db.close()