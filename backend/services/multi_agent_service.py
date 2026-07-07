from graph.workflow import workflow

from services.memory_service import (
    load_memory,
    build_conversation
)


def ask_question(
    question: str,
    session_id: int,
    db
):

    memory = load_memory(
        session_id,
        db
    )

    conversation = build_conversation(
        memory
    )

    result = workflow.invoke(

        {
            "question": question,

            "conversation": conversation,

            "selected_agents": [],

            "retrieved_chunks": [],

            "verified_chunks": [],

            "answer": "",

            "citations": []
        }

    )

    return {

        "answer": result["answer"],

        "sources": result["citations"]

    }