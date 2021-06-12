from app import create_app

app = create_app()
app.app_context().push()

# TODO: rewrite from scratch

'''
def get_weather_in_most_populated_cities():
    with open("cities", "r") as citynames:
        content = citynames.read().splitlines()
    res = []
    for j, city in enumerate(content):
        try:
            print(j, city)
            response_json = WeatherApiClient.get_weather(city, 'F')
            print(response_json)
        except:
            print('Error')
            pass

background_task()
'''