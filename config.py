import os

class Config:
    SECRET_KEY = 'gorgonsonofskrygon'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:james@localhost/blogging'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):

    DEBUG = Truee

config_options = {
    'production': ProdConfig,
    'development':DevConfig,
    'tests': TestConfig
}