"""This module contains the decorator for authenticating requests."""
from functools import wraps
from flask import current_app, request
from jwt import decode, InvalidTokenError, PyJWKClient

def auth_required(func):
    """This decorator is used to authenticate requests to the API."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization') or ''
        token = auth_header.split('Bearer ')[1] if auth_header.startswith('Bearer ') else None
        jwk_url = current_app.config['COGNITO_JWK_URL']

        if token:
            try:
                jwks_client = PyJWKClient(jwk_url)
                signing_key = jwks_client.get_signing_key_from_jwt(token)
                decoded_token = decode(token, signing_key.key, algorithms=['RS256'])
                print(decoded_token)
                return func(*args, **kwargs)
            except InvalidTokenError:
                return {"message": "Invalid token"}, 401
        else:
            return {"message": "Unauthorized"}, 401

    return wrapper
