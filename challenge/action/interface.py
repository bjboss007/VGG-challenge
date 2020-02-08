from typing import List
from mypy_extensions import TypedDict

    
class ActionInterface(TypedDict, total = False):
    id          : int
    name        : str
    description : str
    note        : str
    project_id  : int
    
    