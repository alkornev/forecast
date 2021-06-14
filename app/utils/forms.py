from flask_wtf import FlaskForm
from wtforms.validators import Regexp, ValidationError, DataRequired
from wtforms import StringField


class WeatherForm(FlaskForm):
    """Weather form for weather GET request."""

    cityname = StringField('cityname', validators=[DataRequired(),
                                                   Regexp(regex='[a-zA-Z]+')])
    unit = StringField('password', validators=[DataRequired()])

    def validate_unit(self, unit):
        """Check whether unit equal to C or F shortcut."""
        if unit.data not in ['C', 'F']:
            raise ValidationError("Use only C for Celsius or F for Fahrenheit")
