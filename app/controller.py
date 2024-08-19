from flask_restx import Resource
from flask import request
from .dto import weather_ns, WeatherDto
from .services import get_weather_api
from .extensions import cache

@weather_ns.route('')
class Weather(Resource):
    @weather_ns.doc('get_weather')
    @weather_ns.param('location', 'City name location')
    @weather_ns.response(500, 'Failed to fetch weather data')
    @weather_ns.marshal_with(WeatherDto.weather_model_response)
    @cache.cached(timeout=30, query_string=True)
    def get(self):
        """Fetch weather data from external api"""
        return get_weather_api(request.args.to_dict())
