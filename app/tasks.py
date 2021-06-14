from app import create_app, db
from app.models import Cities
from app.api.weather import WeatherApiClient, WeatherApiError
from sqlalchemy import exc


def background_job():
    """Background job."""
    app = create_app()
    app.app_context().push()
    try:
        cities = Cities()
        for entry in cities.query.all():
            if not entry.fetched:
                entry.fetched = True
                db.session.commit()
                weather = WeatherApiClient.\
                    get_weather(entry.cityname, False)
                WeatherApiClient.save_to_db(weather)
        cities.query.update({'fetched': False})
        db.session.commit()
    except exc.SQLAlchemyError as err:
        print(err)
    except WeatherApiError as err:
        print(err)
