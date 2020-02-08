from challenge import ma
from marshmallow import fields as fl
from marshmallow import INCLUDE, Schema, validates, ValidationError
from challenge.models import User



class UserSchema(ma.Schema):
    username = fl.String(required = True,
                         error_messages = {
                             "required": {
                                 "message":"username is required","code":400
                             }
                         })
    
    password = fl.String(required = True,
                         error_messages = {
                             "required":{
                                 "message":"password is required", "code":400
                             }
                         })
    

    
    @validates("username")
    def validate_user(self, username):
        user = User.query.filter_by(username = username).first()
        if user:
            raise ValidationError("Username already exist, please choose a another username")
        
        