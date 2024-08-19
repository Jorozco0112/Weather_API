from dataclasses import dataclass
from flask_restx import fields, Namespace

weather_ns = Namespace('weather', description="Weather related operations")

@dataclass
class WeatherDto:
    """This class contains weather model to
    serialize the information"""
    # Nested model for 'values'
    values_model = weather_ns.model(
        'Values', {
            'cloudBase': fields.Float(attribute='cloudBase', description="Cloud base height in km"),
            'cloudCeiling': fields.Float(
                attribute='cloudCeiling',
                description="Cloud ceiling height in km"
            ),
            'cloudCover': fields.Integer(
                attribute='cloudCover',
                description="Cloud cover percentage"
            ),
            'dewPoint': fields.Float(
                attribute='dewPoint',
                description="Dew point in °C"
            ),
            'freezingRainIntensity': fields.Float(
                attribute='freezingRainIntensity',
                description="Freezing rain intensity"
            ),
            'humidity': fields.Integer(attribute='humidity', description="Humidity percentage"),
            'precipitationProbability': fields.Integer(
                attribute='precipitationProbability',
                description="Precipitation probability"
            ),
            'pressureSurfaceLevel': fields.Float(
                attribute='pressureSurfaceLevel',
                description="Surface level pressure in hPa"
            ),
            'rainIntensity': fields.Float(attribute='rainIntensity', description="Rain intensity"),
            'sleetIntensity': fields.Float(
                attribute='sleetIntensity',
                description="Sleet intensity"
            ),
            'snowIntensity': fields.Float(attribute='snowIntensity', description="Snow intensity"),
            'temperature': fields.Float(attribute='temperature', description="Temperature in °C"),
            'temperatureApparent': fields.Float(
                attribute='temperatureApparent',
                description="Apparent temperature in °C"
            ),
            'uvHealthConcern': fields.Integer(
                attribute='uvHealthConcern',
                description="UV health concern level"
            ),
            'uvIndex': fields.Integer(attribute='uvIndex', description="UV index"),
            'visibility': fields.Float(attribute='visibility', description="Visibility in km"),
            'weatherCode': fields.Integer(
                attribute='weatherCode',
                description="Weather condition code"
            ),
            'windDirection': fields.Float(
                attribute='windDirection',
                description="Wind direction in degrees"
            ),
            'windGust': fields.Float(attribute='windGust', description="Wind gust speed in km/h"),
            'windSpeed': fields.Float(attribute='windSpeed', description="Wind speed in km/h")
        }
    )

    # Nested model for 'location'
    location_model = weather_ns.model(
        'Location', {
            'lat': fields.Float(attribute='lat', description="Latitude"),
            'lon': fields.Float(attribute='lon', description="Longitude"),
            'name': fields.String(attribute='name', description="Location name"),
            'type': fields.String(attribute='type', description="Location type")
        }
    )

    # Main weather model
    weather_model = weather_ns.model(
        "Weather", {
            'time': fields.String(attribute='general_info', description="Observation time"),
            'values': fields.Nested(values_model, attribute='values_info'),
            'location': fields.Nested(location_model, attribute='location_info')
        }
    )


    weather_model_response = weather_ns.model(
        'weather_model_response',
        {
            'data': fields.Nested(weather_model),
            'success': fields.Boolean(),
            'rowTotal': fields.Integer(),
            'message': fields.String()
        }
    )
