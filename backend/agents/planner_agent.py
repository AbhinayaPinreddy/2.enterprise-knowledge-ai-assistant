import json

from typer import prompt

from graph.state import EnterpriseState
from llm.groq_llm import generate
from llm.groq_llm import generate_answer


def planner_agent(state):
    question = state["question"]

    prompt = f"""
You are an Enterprise AI Planner.

Current Question:

{question}

Available experts:

1. HR
2. Finance
3. IT

Choose which experts should answer the user's question.

Return ONLY JSON.

Example:

{{"agents":["HR"]}}

Question:

{question}
"""
    from llm.groq_llm import generate

    text = generate(prompt)

    # remove markdown if Gemini returns ```json
    text = text.replace("```json", "")
    text = text.replace("```", "").strip()

    data = json.loads(text)

    print("========== PLANNER ==========")
    print(data["agents"])
    print("=============================")

    state["selected_agents"] = data["agents"]

    return state

