from flask import Blueprint, request
from marshmallow import ValidationError
from .schema import ActionSchema
from .service import ActionService
from challenge.project.service import ProjectService
from challenge.models import Action


action = Blueprint("action", __name__, url_prefix="/api")

action_schema = ActionSchema()
action_schemas = ActionSchema(many=True)
action_service = ActionService()
project_service = ProjectService()

@action.route("/projects/<project_id>/actions", methods = ["POST"])
def create_action(project_id):
    req = request.get_json(force=True)
    try:
        data = action_schema.load(req)
        data["project_id"] = project_id
        action = action_service.create(data)
        res = action_schema.dump(action)
        return res, 201
    except ValidationError as err:
        return err.messages, 400
    
@action.route("/actions")
def retrieve_all_actions():
    actions = action_service.get_all()
    res = action_schemas.dump(actions)
    return {"actions": res}, 200
    
@action.route("/projects/<project_id>/actions", methods = ["GET"])
def retrieve_project_actions(project_id):
    try:
        project = project_service.get(project_id)
        actions = project.actions
        res = action_schemas.dump(actions)
        return {"actions":res}, 200
    except Exception:
        return {"message": "data do not exists "}, 401
    

@action.route("/actions/<action_id>", methods = ["GET"])
def get_action(action_id):
    action = action_service.get(action_id)
    if action:
        res = action_schema.dump(action)
        return res, 200
    return {"message": "data do not exists"}, 401


@action.route("/projects/<project_id>/actions/<action_id>", methods = ["GET"])
def retrieve_action(project_id: int, action_id: int):
    project = project_service.get(project_id)
    if project:
        actions = project.actions
        if int(action_id) not in [_action.id for _action in actions]:
            return {"message": "Action does not exists in project"}, 401 
        else:
            data = Action.query.get(int(action_id))
            res = action_schema.dump(data)
            return res, 200  
    return {"message": "project does not exists"}, 401


@action.route("/projects/<project_id>/actions/<action_id>", methods = ["PUT"])
def update_action(project_id: int, action_id: int):
    req = request.get_json(force = True)
    project = project_service.get(project_id)
    if project:
        actions = project.actions
        for action in actions:
            if int(action_id) not in [_action.id for _action in actions]:
                return {"message": "Action does not exists in project"}, 401 
        else:
            try:
                data = action_schema.load(req)
                action_update = action_service.update(action_id, data)
                res = action_schema.dump(action_update)
                return res, 200
            except ValidationError as err:
                return err.messages, 400
    return {"message": "project does not exists"}, 401

@action.route("/projects/<project_id>/actions/<action_id>", methods = ["DELETE"])
def delete_action(project_id: int, action_id: int):
    project = project_service.get(project_id)
    if project:
        actions = project.actions
        if int(action_id) not in [_action.id for _action in actions]:
            return {"message": "Action does not exists in project"}, 401 
        else:
            res = action_service.delete(project_id, action_id)
            return {"message":"Action successfully deleted"}, 200  
    return {"message": "project does not exists"}, 401