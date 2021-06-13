from flask_wtf import FlaskForm
from wtforms import DateTimeField
from wtforms.validators import ValidationError, DataRequired
from app.models import Weather


class PeriodForm(FlaskForm):
    """Base class for validation time period parameters"""
    startdate = DateTimeField('startdate', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    enddate = DateTimeField('enddate', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
