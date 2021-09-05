import os

from dotenv import load_dotenv

load_dotenv()


class Configuration(object):
    DEBUG = os.environ.get("DEBUG")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
