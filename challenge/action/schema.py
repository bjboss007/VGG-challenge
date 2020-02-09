from marshmallow import Schema
from marshmallow import fields as fl
from challenge import ma



class ActionSchema(Schema):
    
    class Meta:
        fields = ("id","name","description","note","project_id","_links")
        ordered = True
        
    name = fl.String(required=True, error_messages={
        "required":{
            "message":"name is required",
            "code": 400
        }
    })
    
    description = fl.String(required=True, error_messages={
        "required":{
            "message":"description is required",
            "code": 400
        }
    })
    
    note = fl.String(required=True, error_messages={
        "required":{
            "message":"note is required",
            "code": 400
        }
    })
    
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("action.get_action", action_id = '<id>'),
            "collections": ma.URLFor("action.retrieve_all_actions"),
            "parent": ma.URLFor("project.retrieve_one_project", id = '<project_id>')
        }
    )
