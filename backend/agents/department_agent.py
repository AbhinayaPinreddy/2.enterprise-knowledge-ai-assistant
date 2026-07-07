from unicodedata import category

from rag.retriever import retrieve

from graph.worker_state import WorkerState


def department_agent(state: WorkerState):

    chunks = retrieve(

        state["question"],

        state["category"]

    )
    print("\n========== RETRIEVED ==========")
    print(state["category"])
    print(len(chunks))

    for r in chunks:
        print(r["document"], r["page"])

    print("===============================\n")

    return {

        "retrieved_chunks": chunks

    }

def hr_agent(state):
    return department_agent(state, "HR")


def finance_agent(state):
    return department_agent(state, "Finance")


def it_agent(state):
    return department_agent(state, "IT")