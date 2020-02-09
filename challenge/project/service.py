from challenge import db
from typing import List
from .interface import ProjectInterface
from challenge.models import Project
from challenge.utils import upload_file

class ProjectService:
    
    @staticmethod
    def get(id : int):
        project = Project.query.get(id)
        return project
    
    @staticmethod
    def create(new_attr: ProjectInterface) -> Project:
        
        new_project = Project(
            name = new_attr["name"],
            description = new_attr["description"],
            completed = new_attr["completed"]
        )
        db.session.add(new_project)
        db.session.commit()
        return new_project
    
    @staticmethod
    def update(id: int , new_attr: ProjectInterface) -> Project:
        project = Project.query.get(id)
        project.name = new_attr["name"]
        project.description = new_attr["description"]
        project.completed = new_attr["completed"]
        
        db.session.commit()
        return project
    
    @staticmethod
    def patch(id: int , new_attr: ProjectInterface) -> Project:
        project = Project.query.get(id)
        project.completed = new_attr["completed"]
        db.session.commit()
        return project
    
    
    @staticmethod
    def delete(id : int) -> Project:
        try:
            project = Project.query.get(id)
            db.session.delete(project)
            db.session.commit()
            return project, 200
        except Exception as err:
            return "Data do not exits !", 400
            
    @staticmethod
    def get_all() -> List[Project]:
        projects = Project.query.all()
        return projects
    
    
    @staticmethod
    def upload_image(id : int, data: ProjectInterface):
        project = Project.query.get(id)
        file_url = upload_file(data["user_stories"])
        project.user_stories = file_url
        db.session.commit()
        
        return project