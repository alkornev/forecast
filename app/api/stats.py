from flask import request, Response
from app.api import bp
from app.utils.stats import StatsApi, StatsApiException
from app.statistics.forms import PeriodForm
from app.api.errors import bad_request


@bp.route('/save_csv', methods=['GET'])
def get_csv():
    """Saves statistics in csv file"""
    form = PeriodForm(request.get_json(),meta={'csrf': False})
    if form.validate_on_submit():
        try:
            csv_data = StatsApi.save_to_csv()
            response = Response(csv_data.get_value())
            response.code = 200
            #return respones.headers['Content-Disposition'] = 'attachment; filename=report.csv'
        except StatsApiException:
            bad_request()
    return Response()