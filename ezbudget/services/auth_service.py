import requests
from flask import current_app
import base64


def request_token(authorization_code):
    domain = current_app.config.get('COGNITO_DOMAIN')
    token_url = 'https://{}/oauth2/token'.format(domain)
    token_payload = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': current_app.config.get('COGNITO_REDIRECT_URI')
    }

    client_id = current_app.config.get('COGNITO_CLIENT_ID')
    client_secret = current_app.config.get('COGNITO_CLIENT_SECRET')
    auth_string = "{}:{}".format(client_id, client_secret)
    auth_string_encoded = base64.b64encode(auth_string.encode()).decode()
    token_headers = {
        'Authorization': "Basic {}".format(auth_string_encoded),
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    token_response = requests.post(token_url, data=token_payload, headers=token_headers)
    token_data = token_response.json()

    return token_data['access_token']
