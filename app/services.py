import requests
from flask import abort
from .constants import API_KEY


def get_weather_api(args:dict):
    """This function request to a
    third party library and return the 
    important data by given parameters
    Input:
        args:dict
    """

    required_fields = {
        "location": "Debe enviar el nombre de la ciudad, es un campo requerido",
    }

    for attr, value in required_fields.items():
        if args.get(attr) is None or args.get(attr) == "":
            abort(
                400,
                {
                    "error": "required fields is empty",
                    "message": value
                }
            )

    location = args['location']
    secret_key = API_KEY
    headers = {"accept": "application/json"}

    # Build the query parameters and URL
    params = {
        "location": location,
        "apikey": secret_key
    }

    weather_url = "https://api.tomorrow.io/v4/weather/realtime"

    response = requests.get(weather_url, headers=headers, params=params, timeout=30)

    # Check if the response status code is not 200 or 201
    if response.status_code not in (200, 201):
        abort(
            502,  # 502 Bad Gateway status code for external service errors
            {
                "error": "External API Error",
                "message": (
                    f"External weather API returned a status code of {response.status_code}. "
                    "The service might be down."
                )
            }
        )


    parsed_response= response.json()
    general_info = parsed_response.get('data').get('time')
    values_info = parsed_response.get('data').get('values')
    location_info = parsed_response.get('location')

    return {
        'success': True,
        'message': f"Información del clima de la localidad de {location}",
        'data': {
            'general_info': general_info,
            'location_info': location_info,
            'values_info': values_info
        },
        'rowTotal': 1
    }
