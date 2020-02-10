import os


class Config():
    SECRETKEY = os.environ.get('SECRETKEY')
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')


class Production(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = False
    
   
