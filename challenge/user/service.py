from challenge import db
from typing import List
from flask import jsonify
from .interface import UserInterface
from challenge.models import User
from flask_jwt_extended import create_access_token

class UserService:
    
    @staticmethod
    def create(new_attr: UserInterface) -> User:
        print("This is the new user : ",new_attr["username"])
        new_user = User(
            username = new_attr["username"],
            password = new_attr["password"]
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
            
    @staticmethod
    def get(id : int) -> User:
        action = User.query.get(id)
        return action
    
    @staticmethod
    def get_all() -> List[User]:
        users = User.query.all()
        return users
    
    @staticmethod
    def login_user(user: UserInterface) -> User:
        user = User.query.filter_by(username = user["username"]).first()
        if user:
            access_token = create_access_token(identity=user.username)
            return jsonify ({"access_token" :access_token})
        return jsonify({"message":"User not found"}), 401