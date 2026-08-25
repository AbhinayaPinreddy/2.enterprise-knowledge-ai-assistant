import numpy as np

from rag.embeddings import get_model
from rag.vector_store import VectorStore

from database import SessionLocal
from models import DocumentChunk, Document


def retrieve(query, category, top_k=10):

    store = VectorStore()

    db = SessionLocal()

    try:

        # Load the embedding model only when retrieval is needed
        model = get_model()

        query_embedding = model.encode(
            [query],
            convert_to_numpy=True
        ).astype(np.float32)

        distances, indices = store.search(
            query_embedding,
            top_k
        )

        results = []

        for distance, idx in zip(distances[0], indices[0]):

            if idx == -1:
                continue

            chunk = db.query(DocumentChunk).filter(
                DocumentChunk.faiss_index == int(idx)
            ).first()

            if chunk is None:
                continue

            document = db.query(Document).filter(
                Document.id == chunk.document_id
            ).first()

            if document is None:
                continue

            if category is not None:

                if document.category.lower() != category.lower():
                    continue

            results.append({
                "score": float(distance),
                "text": chunk.text,
                "document_id": document.id,
                "document": document.filename,
                "page": chunk.page
            })

        for chunk in results:
            print(chunk["page"])
            print(chunk["text"][:200])
            print("----------------")

        return results

    finally:
        db.close()