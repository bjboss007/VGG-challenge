from flask import Blueprint, request
from marshmallow import ValidationError
from .service import ProjectService
from .schema import ProjectSchema, ProjectPatchSchema
from challenge.models import Project
from challenge.utils import upload_file
from sqlalchemy import or_



project = Blueprint("project", __name__, url_prefix="/api")

project_schema = ProjectSchema()
patchSchema = ProjectPatchSchema()
project_schemas = ProjectSchema(many=True)
project_service = ProjectService()

@project.route("/projects", methods = ["POST"])
def create_project():
    req = request.get_json(force = True)
    
    try:
        data = project_schema.load(req)
        project = project_service.create(data)
        res = project_schema.dump(project)
        return res, 201
    except ValidationError as err:
        return err.messages

@project.route("/projects", methods = ["GET"])
def retrieve_all_project():
    args = request.args
    # print(ret)
    try:
        if "search" in args:
            search = request.args["search"]
            result = Project.query.filter(or_(Project.name.like(search),Project.description.like(search))).first()
            if result:
                response = project_schema.dump(result)
                return response, 200
            else:
                return {"message":f"{search} not found"}, 401
            
        if ("offset" in args) and ("limit" in args):
            offset = int(request.args["offset"])
            limit = int(request.args["limit"])
            proj = Project.query.paginate(page=offset, per_page = limit).items
            respose = project_schemas.dump(proj)
            return {"projects" : respose}, 200
        
    except Exception:
        return {"message" : "An error occurred"}, 500
    projects = project_service.get_all()
    res = project_schemas.dump(projects)
    return {"projects" : res}, 200
    
    
@project.route("/projects/<id>", methods = ["GET"])
def retrieve_one_project(id):
    project = project_service.get(id)
    if project:
        res = project_schema.dump(project)
        return res, 200
    return {"message": "data do not exists"}, 401

@project.route("/projects/<id>", methods = ["PUT"])
def update_project(id):
    req = request.get_json(force = True)
    try:
        data = project_schema.load(req)
        project = project_service.update(id, data )
        res = project_schema.dump(project)
        return res, 200
    except ValidationError as err:
        return err.messages
    
@project.route("/projects/<id>", methods = ["PATCH"])
def update_project_attr(id):
    req = request.get_json(force = True)
    try:
        data = patchSchema.load(req)
        project = project_service.patch(id, data)
        res = project_schema.dump(project)
        return res, 201
    except ValidationError as err:
        return err.messages


@project.route("/projects/<id>", methods = ["DELETE"])
def delete_project(id):
    res = project_service.delete(id)
    return res


@project.route("/projects/<project_id>/upload", methods=["POST"])
def upload(project_id: int):
    req = request.get_json(force = True)
    data = patchSchema.load(req)
    project = project_service.upload_image(project_id,data)
    res = project_schema.dump(project)
    return res, 200
    