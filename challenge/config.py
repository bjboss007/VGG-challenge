import os


class Config():
    SECRETKEY = 'eab3cbb80cc6459864c930ebd9d29dea'
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    JWT_SECRET_KEY = '7d9b829544b4c258cb91ddfd4b5a9801'


class Production(Config):
    SECRETKEY = 'eab3cbb80cc6459864c930ebd9d29dea'
    SQLALCHEMY_DATABASE_URI = "postgres://svklzrvsnbcqqt:eb5fde5a027be5ea0059bb9d5bb328950e6d228010e9076fba3000d6631452dd@ec2-18-213-176-229.compute-1.amazonaws.com:5432/db66hh7reqtt87"
    DEBUG = False
    