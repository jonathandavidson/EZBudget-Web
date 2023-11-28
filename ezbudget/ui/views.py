from ezbudget.services.auth_service import request_token
from flask import Blueprint, render_template, request

ui = Blueprint('ui', __name__)

@ui.route('/')
def home():
    return render_template('home.html')

@ui.route('/auth/signin', methods=['GET'])
def signin():
    code = request.args.get('code')
    
    token = request_token(code);
    # Your code logic here
    return 'Signin GET request received with code: {}'.format(code)
