from rag.pdf_loader import extract_pages_from_pdf
from rag.chunker import split_pages_into_chunks
from rag.embeddings import generate_embeddings


def process_document(pdf_path, document_id):

    pages = extract_pages_from_pdf(pdf_path)

    chunks = split_pages_into_chunks(
        pages,
        document_id
    )

    embeddings = generate_embeddings(chunks)

    processed_chunks = []

    for chunk, embedding in zip(chunks, embeddings):

        processed_chunks.append({
            "chunk_id": chunk["chunk_id"],
            "document_id": chunk["document_id"],
            "page": chunk["page"],
            "text": chunk["text"],
            "embedding": embedding
        })

    return processed_chunks