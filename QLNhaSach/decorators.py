from functools import wraps
from flask_login import current_user
from flask import redirect


def annonymous_user(f):
    @wraps(f)
    def decorated_func(*args, **kwrags):
        if current_user.is_authenticated:
            return redirect('/')
        return f(*args, **kwrags)
    return decorated_func