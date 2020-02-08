import os


class Config():
    SECRETKEY = 'eab3cbb80cc6459864c930ebd9d29dea'
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    JWT_SECRET_KEY = '7d9b829544b4c258cb91ddfd4b5a9801'


class Production(Config):
    SECRETKEY = os.environ.get("secret_key")
    SQLALCHEMY_DATABASE_URI = os.environ.get('database_uri')
    DEBUG = False
    