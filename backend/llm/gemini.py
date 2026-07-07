import google.generativeai as genai

from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(question, retrieved_chunks, conversation):

    context = ""

    for chunk in retrieved_chunks:

        context += chunk["text"]
        context += "\n\n"

    prompt = f"""
You are an Enterprise Knowledge Assistant.

Answer ONLY from the given context.

If the answer is not present,
reply exactly:

'I couldn't find that information in the uploaded documents.'
Conversation History:
{conversation}

Retrieved Context:
{context}

Current Question:
{question}
"""
    print("\n========== CONTEXT ==========")
    print(context)
    print("============================\n")
    response = model.generate_content(prompt)

    return response.text