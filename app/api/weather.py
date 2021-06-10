from app.api.auth import token_auth
from app.api import bp
from app import UNITS
from flask import request, jsonify, Response
import requests
from requests.exceptions import HTTPError, RequestException
from config import Config
from app.api.errors import bad_request, error_response
from app import cache

@bp.route('/weather', methods=['GET'])
@token_auth.login_required
@cache.cached(timeout=60, query_string=True)
def get_weather() -> Response:
    """Requests temperature in given city in Celsius or Fahrenheit"""
    cityname = request.args.get('cityname', None)
    short_unit = request.args.get('unit', 'C')
    # if unit is invalid use Celsius
    if short_unit != 'C' and short_unit != 'F':
        short_unit = 'C'
    unit = UNITS[short_unit]

    if not cityname:
        return bad_request("Please enter city name")
    if not cityname.isalpha():
        return bad_request("Please use only latin characters")

    api_key = Config.USER_OWM_APIKEY
    api_url = Config.OWM_LINK
    try:
        response = requests.get(
            api_url,
            params={
                'q': cityname,
                'units': unit,
                'appid': api_key
            }
        )
        response.raise_for_status()
        data = response.json()
        return jsonify({'City name': cityname,
                        'temp': data['main']['temp'],
                        'units': short_unit})
    except HTTPError as http_err:
        # TODO: return more detailed output on error
        return error_response(response.status_code, str(http_err))
    except RequestException as err:
        return bad_request("Error!")
