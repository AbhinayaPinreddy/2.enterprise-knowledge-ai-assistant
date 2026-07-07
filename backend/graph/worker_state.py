from typing import Annotated
from typing_extensions import TypedDict
import operator


class WorkerState(TypedDict):

    question: str

    category: str

    retrieved_chunks: Annotated[list, operator.add]