from challenge import db, bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(225), unique = True, nullable = False)
    password = db.Column(db.String(225), nullable = False)
    
    def __init__(self, *args, **kwargs):
        self.username = kwargs["username"]
        self.password = bcrypt.generate_password_hash(kwargs["password"]).decode('utf-8')
        
        
    def __repr__(self):
        return f"User => [ '{self.username}' ]"

class Project(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String, nullable = False)
    completed = db.Column(db.Boolean, nullable = False)
    actions = db.relationship('Action', backref = 'project', lazy = True)
    user_stories = db.Column(db.String, nullable = True)
    
    def __repr__(self):
        return f"Project => [ '{self.name}' ]"
    
class Action(db.Model):
    id = db.Column(db.Integer,unique = True, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String, nullable = False)
    note = db.Column(db.String, nullable = False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable = False)
    
    def __repr__(self):
        return f"Action => [ '{self.name}' ]"