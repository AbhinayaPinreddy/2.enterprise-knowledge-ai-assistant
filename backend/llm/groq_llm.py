from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

MODEL = "llama-3.3-70b-versatile"


def generate(prompt: str):

    response = client.chat.completions.create(

        model=MODEL,

        temperature=0,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    return response.choices[0].message.content


def generate_answer(question, retrieved_chunks, conversation):

    context = ""

    for chunk in retrieved_chunks:

        context += chunk["text"] + "\n\n"

    prompt = f"""
You are an Enterprise Knowledge Assistant.

Conversation History:
{conversation}

Retrieved Context:
{context}

Current Question:
{question}

Instructions:

- Answer ONLY from the retrieved context.
- If the answer is not present in the retrieved context, reply exactly:
"I couldn't find that information in the uploaded documents."

- Never make up information.
- Quote only facts supported by the retrieved context.
- Give a concise answer.
"""

    return generate(prompt)