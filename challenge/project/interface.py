from typing import List
from mypy_extensions import TypedDict


class ProjectInterface(TypedDict, total = False):
    id          : int
    name        : str
    description : str
    completed   : bool

    