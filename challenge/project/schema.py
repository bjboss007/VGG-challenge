from challenge import ma
from marshmallow import fields as fl
from marshmallow import INCLUDE, Schema, validates, ValidationError
from challenge.models import Project



class ProjectSchema(Schema):
    class Meta:
        fields = ("id","name","description","completed","_links")
        ordered = True
        
    name = fl.String(required= True, error_messages={
        "required": {
            "message":"name is required", 
            "code": 400
        }
    })
    
    description = fl.String(required= True, error_messages={
        "required": {
            "message":"description is required", 
            "code": 400
        }
    })
     
    completed  = fl.Boolean()
    
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("project.retrieve_one_project", id = '<id>'),
            "collections": ma.URLFor("project.retrieve_all_project"),
            "actions": ma.URLFor("action.retrieve_project_actions", project_id = '<id>')
        }
    )
    
class ProjectPatchSchema(Schema):
    class Meta:
        fields = ["completed"]
        ordered = True
    
    completed  = fl.Boolean()