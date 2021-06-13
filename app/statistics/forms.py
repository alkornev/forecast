from flask_wtf import FlaskForm
from wtforms import DateTimeField
from wtforms.validators import ValidationError, DataRequired
from app.models import Weather


class PeriodForm(FlaskForm):
    startdate = DateTimeField('startdate', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    enddate = DateTimeField('enddate', format='%Y-%m-%d %H:%M', validators=[DataRequired()])

    def validate_startdate(self, startdate):
        pass
        #weather = Weather.query.filter(Weather.datetime <
        #                               startdate.datetime).order_by(asc(Weather_date))
        #if weather is None:
        #    raise ValidationError('Try another startdate.')

    def validate_enddate(self, enddate):
        pass
        #weather = Weather.query.filter(email=enddate.data).first()
        #if weather :
        #    raise ValidationError('Try another enddate.')

    def validate_dates(self, startdate, enddate):
        if startdate.data > enddate.data:
            raise ValidationError('Startdate should be less than enddate.')
