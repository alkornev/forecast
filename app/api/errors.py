from flask import jsonify, Response
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code: int, message=None) -> Response:
    """returns error status with message """
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


def bad_request(message) -> Response:
    """returns 400 error code"""
    return error_response(400, message)
