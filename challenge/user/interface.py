from typing import List
from mypy_extensions import TypedDict

    
class UserInterface(TypedDict, total = False):
    id       : int
    username : str
    password : str
    
    
    