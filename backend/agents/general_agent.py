from llm.groq_llm import generate,generate_answer


def general_agent(state):

    prompt = f"""
You are an Enterprise Knowledge Assistant.

Respond naturally and professionally.

Do NOT answer using enterprise documents.

If asked what you do, explain that you help employees find information from uploaded enterprise documents such as HR, Finance, IT and Security policies.

Keep the response friendly and concise.

Conversation:
{state["conversation"]}

User:
{state["question"]}
"""

    answer = generate(prompt)

    return {
    "answer": answer,
    "citations": []
}