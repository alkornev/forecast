import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    """Config class containing environment variables"""
    SECRET_KEY: str = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    LOG_TO_STDOUT: str = os.environ.get('LOG_TO_STDOUT')
    USER_OWM_APIKEY: str = "f90a79d425d1a3a1b4574e3d3282fa86"
    DB_OWN_APIKEY: str = "a974e24678134ed625182468e4a72f63"
    OWM_LINK: str = "http://api.openweathermap.org/data/2.5/weather"

