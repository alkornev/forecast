from flask import Response
from app import db
from app.errors import bp
from app.api.errors import error_response as api_error_response
from app import cache


@bp.app_errorhandler(404)
@cache.cached(timeout=60)
def not_found_error(error) -> Response:
    return api_error_response(404)


@bp.app_errorhandler(500)
@cache.cached(timeout=60)
def internal_error(error) -> Response:
    db.session.rollback()
    return api_error_response(500)
