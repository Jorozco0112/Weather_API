from flask_restx import Resource
from flask import request
from .dto import weather_ns, WeatherDto
from .services import get_weather_api


@weather_ns.route('/')
class Weather(Resource):
    @weather_ns.doc('get_weather')
    @weather_ns.param('city', 'The city name')
    @weather_ns.response(200, 'Success', WeatherDto.weather_model)
    @weather_ns.response(400, 'City parameter is required')
    @weather_ns.response(500, 'Failed to fetch weather data')
    def get(self):
        """Fetch weather data from external api"""
        return get_weather_api(request.args.to_dict())
