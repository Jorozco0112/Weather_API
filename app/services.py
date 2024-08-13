import openmeteo_requests


def get_weather_api(args:dict):
    """This function request to a
    third party library and return the 
    important data by given parameters
    Input:
        args:dict
    """

    open_meteo = openmeteo_requests.Client()

    weather_url = "https://api.open-meteo.com/v1/forecast"

    api_response = open_meteo.weather_api(weather_url, params=args)
