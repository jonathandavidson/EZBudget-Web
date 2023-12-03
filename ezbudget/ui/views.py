"""Views for the UI module."""
from urllib.parse import urlencode
from flask import Blueprint, render_template, redirect, request, current_app
from ezbudget.services.auth_service import request_token

ui = Blueprint('ui', __name__)


@ui.route('/')
def home():
    """Render the home page."""
    return render_template('home.html')


@ui.route('/login', methods=['GET'])
def login():
    """Redirect to the Cognito hosted UI."""
    domain = current_app.config.get('COGNITO_DOMAIN')
    query_params = {
        'client_id': current_app.config.get('COGNITO_CLIENT_ID'),
        'response_type': 'code',
        'redirect_uri': current_app.config.get('COGNITO_REDIRECT_URI')
    }
    query_string = urlencode(query_params)
    authorize_url = f'https://{domain}/oauth2/authorize?{query_string}'

    return redirect(authorize_url)


@ui.route('/authenticate', methods=['GET'])
def signin():
    """Handle the redirect from the Cognito hosted UI."""
    code = request.args.get('code')
    token = request_token(code)
    # Your code logic here
    return f'Got token from oauth: {token}'
