
from typing import Literal
from .domain import word_count,char_count,reverse

Operazione = Literal["word_count", "char_count","reverse"]

OPERAZIONE = {
    "word_count":word_count,
    "char_count":char_count,
    "reverse":reverse
}

def execute_operation(text: str, operation: Operazione) -> int | str:
    return OPERAZIONE[operation](text)