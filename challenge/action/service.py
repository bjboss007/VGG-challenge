from challenge import db
from typing import List
from .interface import ActionInterface
from challenge.models import Action

class ActionService: 
    @staticmethod
    def create(new_attr: ActionInterface) -> Action:
        
        new_action = Action(
            name = new_attr["name"],
            description = new_attr["description"],
            note = new_attr["note"],
            project_id = new_attr["project_id"]
        )
        db.session.add(new_action)
        db.session.commit()
        return new_action
    
    
    @staticmethod
    def delete(id : int) -> Action:
        action = Action.query.get(id)
        db.session.delete(action)
        db.session.commit()
        
    @staticmethod
    def get(id : int):
        action = Action.query.get(id)
        return action
    
    
    @staticmethod
    def get_all() -> List[Action]:
        actions = Action.query.all()
        return actions