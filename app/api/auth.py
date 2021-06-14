from flask import Response
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.models import User
from app.api.errors import error_response


basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(username: str, password: str) -> User:
    """Take username and password and return User object from db."""
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user


@basic_auth.error_handler
def basic_auth_error(status: int) -> Response:
    """Return error response if not authenticated."""
    return error_response(status)


@token_auth.verify_token
def verify_token(token: str) -> User:
    """Return User object if token exists."""
    return User.check_token(token) if token else None


@token_auth.error_handler
def token_auth_error(status: int) -> Response:
    """Handle auth error handler."""
    return error_response(status)
