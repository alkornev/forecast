from app.api.auth import token_auth
from app.api import bp
from flask import request, jsonify, Response
from app.api.errors import bad_request
from app.utils.weather import WeatherApiError, WeatherApiClient
from app.utils.forms import WeatherForm


@bp.route('/weather', methods=['GET'])
@token_auth.login_required
def get_weather() -> Response:
    """Request temperature in a given city in Celsius or Fahrenheits."""
    form = WeatherForm(request.args, meta={'csrf': False})
    if form.validate():
        try:
            data = WeatherApiClient.get_weather(request.args.get('cityname'))
            if request.args.get('unit') == 'C':
                del data['F']
            else:
                del data['C']
            return jsonify(data)
        except WeatherApiError as err:
            return bad_request(str(err))
    return bad_request("Invalid input parameters")
