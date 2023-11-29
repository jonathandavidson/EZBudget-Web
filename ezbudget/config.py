from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

COGNITO_CLIENT_ID = environ.get('COGNITO_CLIENT_ID')
COGNITO_CLIENT_SECRET = environ.get('COGNITO_CLIENT_SECRET')
COGNITO_DOMAIN = environ.get('COGNITO_DOMAIN')
COGNITO_REDIRECT_URI = environ.get('COGNITO_REDIRECT_URI')
COGNITO_USER_POOL_ID = environ.get('COGNITO_USER_POOL_ID')
COGNITO_REGION_NAME = environ.get('COGNITO_REGION_NAME')
