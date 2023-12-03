"""Authentication service module."""
import base64
import requests
from flask import current_app


def request_token(authorization_code):
    """This function requests a token from Cognito."""
    domain = current_app.config.get('COGNITO_DOMAIN')
    token_url = f'https://{domain}/oauth2/token'

    token_payload = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': current_app.config.get('COGNITO_REDIRECT_URI')
    }

    client_id = current_app.config.get('COGNITO_CLIENT_ID')
    client_secret = current_app.config.get('COGNITO_CLIENT_SECRET')
    auth_string = f'{client_id}:{client_secret}'
    auth_string_encoded = base64.b64encode(auth_string.encode()).decode()

    token_headers = {
        'Authorization': f'Basic {auth_string_encoded}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    token_response = requests.post(token_url,
        data=token_payload,
        headers=token_headers,
        timeout=5)

    token_data = token_response.json()

    return token_data['access_token']
