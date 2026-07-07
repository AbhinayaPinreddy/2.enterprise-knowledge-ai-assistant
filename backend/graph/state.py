from typing import Annotated
from typing_extensions import TypedDict
import operator


class EnterpriseState(TypedDict):

    question: str
    
    intent:str
    
    conversation: str

    selected_agents: list[str]

    category: str

    retrieved_chunks: Annotated[list, operator.add]

    verified_chunks: list

    answer: str

    citations: list