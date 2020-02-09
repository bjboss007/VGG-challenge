from challenge import create_app
from challenge.models import Project
from challenge import db


app = create_app()
app.app_context().push()
if __name__ == "__main__":
    
    try:
        counter = len(Project.query.all()) 
    except Exception:
        db,drop()
        db.create_all()
    app.run(port = 8083)