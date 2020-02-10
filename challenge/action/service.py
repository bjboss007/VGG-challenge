from challenge import db
from typing import List
from .interface import ActionInterface
from challenge.models import Action
from challenge.project.service import ProjectService

project_service = ProjectService()

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
    def update(id: int, new_action: ActionInterface) -> Action:
        action = Action.query.get(id)
        action.name = new_action["name"]
        action.description = new_action["description"]
        action.note = new_action["note"] 
        
        db.session.commit()
        return action
    
    @staticmethod
    def delete(project_id: int, action_id: int):
        project = project_service.get(project_id)
        action = Action.query.get(action_id)
        
        project.actions.remove(action)
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
