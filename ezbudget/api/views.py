from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/endpoint')
def api_endpoint():
    return {"message": "Hello from API!"}
