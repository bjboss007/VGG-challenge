from flask import Blueprint, request, abort
from .schema import UserSchema
from .service import UserService
from marshmallow import ValidationError



user = Blueprint("user", __name__, url_prefix="/api")


user_schema = UserSchema()
user_service = UserService()

@user.route("/users/register", methods = ["POST", "GET"])
def register():
    req = request.get_json(force=True)
    try:
        data = user_schema.load(req)
        user = user_service.create(data)
        res = user_schema.dump(user)
        return res
    except ValidationError as err:
        return err.messages, 400
    

@user.route("/users/auth", methods = ["POST"])
def get_token():
    req = request.get_json(force=True)
    res = user_service.login_user(req)
    return res