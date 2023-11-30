from flask import request
from functools import wraps

def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.headers.get('Authorization') == 'Bearer 123':
            return func(*args, **kwargs)
        else:
            return {"message": "Unauthorized"}, 401
    return wrapper
  