from marshmallow import Schema
from marshmallow import fields as fl



class ActionSchema(Schema):
    
    class Meta:
        fields = ("id","name","description","note","project_id")
        ordered = True
        
    name = fl.String(required=True, error_messages={
        "required":{
            "message":"name is required"
        }
    })
    
    description = fl.String(required=True, error_messages={
        "required":{
            "message":"description is required"
        }
    })
    
    note = fl.String(required=True, error_messages={
        "required":{
            "message":"note is required"
        }
    })
    
    