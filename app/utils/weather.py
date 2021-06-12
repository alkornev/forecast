import requests
from datetime import datetime, timedelta
from app.models import Weather
from app import db

UNITS = {'F': 'imperial', 'C': 'metric'}


class WeatherApiError(Exception):
    """Base class for weather api http request exceptions"""
    pass


class WeatherApiClient:
    """Base class for weather api http requests"""
    API_KEY: str = "f90a79d425d1a3a1b4574e3d3282fa86"
    OWA_URL: str = "http://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def to_fahr(celsius: float):
        """Converts celsius to fahrenheit degrees"""
        return round(9 / 5 * celsius + 32, 2)

    @classmethod
    def get_weather(cls, cityname: str) -> dict:
        """Return weather from OWA, first search in db then makes request"""
        try:
            weather = Weather()
            # check if there is any record in db in last minute
            cached = Weather.query.filter(Weather.cityname == cityname,
                                          Weather.datetime >=
                                          datetime.utcnow() -
                                          timedelta(seconds=60)).first()
            if cached:
                return cached.to_dict()

            params = {'q': cityname, 'units': 'metric', 'appid': cls.API_KEY}
            response = requests.get(cls.OWA_URL, params=params)
            response.raise_for_status()
            data = response.json()
            result = {'cityname': cityname,
                      'datetime': datetime.utcnow(),
                      'C': data['main']['temp'],
                      'F': cls.to_fahr(data['main']['temp'])}
            weather.from_dict(result)
            db.session.add(weather)
            db.session.commit()
            return result
        except requests.HTTPError as err:
            raise WeatherApiError('call to OWA failed') from err
