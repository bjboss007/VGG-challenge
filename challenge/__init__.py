from flask import Flask
from flask_marshmallow import Marshmallow
from challenge.config import Config, Production
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import cloudinary as Cloud
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()



def create_app(config_class = Production):
    app = Flask(__name__)
    
    app.config.from_object(config_class)
    ma.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    with app.app_context():
        from challenge.project.routes import project
        from challenge.action.routes import action
        from challenge.user.routes import user
        
        app.register_blueprint(project)
        app.register_blueprint(action)
        app.register_blueprint(user)
        
        return app