from rag.retriever import retrieve
from llm.gemini import generate_answer


def ask_question(question: str):

    retrieved_chunks = retrieve(question)

    if len(retrieved_chunks) == 0:

        return {
            "answer": "I couldn't find any relevant information in the uploaded documents.",
            "sources": []
        }

    answer = generate_answer(
        question,
        retrieved_chunks
    )

    sources = []

    seen = set()

    for chunk in retrieved_chunks:

        key = (chunk["document"], chunk["page"])

        if key not in seen:

            seen.add(key)

            sources.append({
                "document_id": chunk["document_id"],
                "document": chunk["document"],
                "page": chunk["page"]
            })

    return {
        "answer": answer,
        "sources": sources
    }