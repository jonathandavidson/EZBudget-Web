from ezbudget.services.auth_service import request_token
from flask import Blueprint, render_template, redirect, request, current_app
from urllib.parse import urlencode

ui = Blueprint('ui', __name__)

@ui.route('/')
def home():
    return render_template('home.html')

@ui.route('/login', methods=['GET'])
def login():
    domain = current_app.config.get('COGNITO_DOMAIN')
    query_params = {
        'client_id': current_app.config.get('COGNITO_CLIENT_ID'),
        'response_type': 'code',
        'redirect_uri': current_app.config.get('COGNITO_REDIRECT_URI')
    }
    query_string = urlencode(query_params)
    authorize_url = "https://{}/oauth2/authorize?{}".format(domain, query_string)

    return redirect(authorize_url)

@ui.route('/authenticate', methods=['GET'])
def signin():
    code = request.args.get('code')
    token = request_token(code);
    # Your code logic here
    return 'Got token from oauth: {}'.format(token)
