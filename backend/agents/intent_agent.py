import json
from llm.groq_llm import generate


def intent_agent(state):

    question = state["question"]

    prompt = f"""
You are an Intent Classification Agent for an Enterprise Knowledge Assistant.

Your job is to classify the user's query into exactly ONE of the following intents.

1. GENERAL
Use GENERAL if the user is:
- greeting you
- asking who you are
- asking what you can do
- asking for help
- thanking you
- saying goodbye
- engaging in normal conversation
- asking about your capabilities
- asking any question that does NOT require information from enterprise documents.

2. DOCUMENT
Use DOCUMENT if answering requires information from uploaded enterprise documents such as:
- HR policies
- Leave policy
- Payroll
- Finance
- IT
- Security
- Company handbook
- Reimbursements
- Attendance
- Benefits
- Any enterprise-specific information.

Return ONLY valid JSON.

Example:

{{"intent":"GENERAL"}}

or

{{"intent":"DOCUMENT"}}

Question:
{question}
"""

    text = generate(prompt)

    text = text.replace("```json", "")
    text = text.replace("```", "").strip()

    data = json.loads(text)
    print("\n========== INTENT ==========")
    print(question)
    print(data["intent"])
    print("============================\n")

    state["intent"] = data["intent"]

    return state