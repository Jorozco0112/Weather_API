from dataclasses import dataclass
from flask_restx import fields, Namespace

weather_ns = Namespace('weather', description="Weather related operations")

@dataclass
class WeatherDto:
    """This class contains weather model to
    serialize the information"""
    weather_model = weather_ns.model(
        "Weather",
        {
            'city':fields.String(description="City name"),
            'temperature': fields.String(description="Current temperature"),
            'description': fields.String(description="weather description")
        }
    )
