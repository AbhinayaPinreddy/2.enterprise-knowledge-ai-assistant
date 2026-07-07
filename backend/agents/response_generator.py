from llm.groq_llm import generate_answer

def response_generator(state):

    answer = generate_answer(

        state["question"],

        state["verified_chunks"],

        state["conversation"]

    )

    return {

        "answer": answer

    }