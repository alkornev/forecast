import io
import csv
from app.api.auth import token_auth
from flask import request, Response
from app.api import bp
from app.models import Weather
from app.stats.forms import PeriodForm
from app.api.errors import bad_request


@bp.route('/stats', methods=['GET'])
@token_auth.login_required
def get_csv() -> Response:
    """Save statistics in csv file."""
    form = PeriodForm(request.args, meta={'csrf': False})

    if not form.validate():
        return bad_request("Bad input parameters")

    start = form.startdate.data
    end = form.enddate.data

    csv_data = io.StringIO()
    writer = csv.DictWriter(csv_data, ['cityname', 'datetime', 'C', 'F'])
    writer.writeheader()
    for item in Weather.query.filter(start <= Weather.datetime,
                                     Weather.datetime <= end).all():
        writer.writerow(item.to_dict())
    response = Response(csv_data.getvalue())
    response.code = 200
    response.headers['Content-Disposition'] = 'attachment; filename=report.csv'

    return response
