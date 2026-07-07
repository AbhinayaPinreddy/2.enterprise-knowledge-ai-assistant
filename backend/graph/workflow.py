from langgraph.graph import StateGraph, START, END
from langgraph.types import Send

from graph.state import EnterpriseState
from graph.worker_state import WorkerState

from agents.intent_agent import intent_agent
from agents.general_agent import general_agent
from agents.planner_agent import planner_agent
from agents.department_agent import department_agent
from agents.verification_agent import verification_agent
from agents.citation_agent import citation_agent
from agents.response_generator import response_generator


# ---------------------------------------
# Route after Intent Agent
# ---------------------------------------

def route_intent(state: EnterpriseState):

    if state["intent"] == "GENERAL":
        return "general"

    return "planner"


# ---------------------------------------
# Parallel Department Workers
# ---------------------------------------

def assign_workers(state: EnterpriseState):

    sends = []

    for category in state["selected_agents"]:

        sends.append(

            Send(

                "department_agent",

                {
                    "question": state["question"],
                    "category": category
                }

            )

        )

    return sends


# ---------------------------------------
# Build Graph
# ---------------------------------------

builder = StateGraph(EnterpriseState)

builder.add_node("intent", intent_agent)

builder.add_node("general", general_agent)

builder.add_node("planner", planner_agent)

builder.add_node("department_agent", department_agent)

builder.add_node("verification", verification_agent)

builder.add_node("citation", citation_agent)

builder.add_node("response", response_generator)


# ---------------------------------------
# Start
# ---------------------------------------

builder.add_edge(START, "intent")


# ---------------------------------------
# Intent Routing
# ---------------------------------------

builder.add_conditional_edges(

    "intent",

    route_intent,

    {

        "general": "general",

        "planner": "planner"

    }

)


# ---------------------------------------
# Planner → Parallel Workers
# ---------------------------------------

builder.add_conditional_edges(

    "planner",

    assign_workers,

    ["department_agent"]

)


# ---------------------------------------
# Remaining Flow
# ---------------------------------------

builder.add_edge("department_agent", "verification")

builder.add_edge("verification", "citation")

builder.add_edge("citation", "response")

builder.add_edge("response", END)

builder.add_edge("general", END)


# ---------------------------------------
# Compile
# ---------------------------------------

workflow = builder.compile()