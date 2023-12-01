from flask import current_app, request
from functools import wraps
from jwt import decode, InvalidTokenError, PyJWKClient

def auth_required(func):
    @wraps(func)

    def wrapper(*args, **kwargs):
        authHeader = request.headers.get('Authorization')
        token = authHeader.split('Bearer ')[1] if authHeader.startswith('Bearer ') else None
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
  