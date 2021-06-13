from rq import get_current_job
from app import create_app, db
from app.models import Cities
from app.api.weather import WeatherApiError, WeatherApiClient
import time


app = create_app()
app.app_context().push()


def background_job():
    """Background job"""
    cities = Cities()
    try:
        for entry in cities.query.all():
            if not entry.fetched:
                entry.fetched = True
                db.session.commit()
                weather = WeatherApiClient.\
                    get_weather(entry.cityname, to_db=True)
        cities.query.update({'fetched': False})
        db.session.commit()
    except WeatherApiError as err:
        # wait 1 minute until weather api limitation will be expired
        time.sleep(60)
        print('Waiting API...')
    except Exception as err:
        print("db related problem")

    print('Task completed!')
    print(" I'm going to sleep...")
    time.sleep(70)


app.task_queue.enqueue(background_job)



