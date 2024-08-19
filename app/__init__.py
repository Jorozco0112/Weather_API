from flask import Flask
from .extensions import api, cache
from .controller import weather_ns
from .config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize the extensions
    api.init_app(app)
    cache.init_app(app)
    # Add the Weather API namespace
    api.add_namespace(weather_ns, path='/weather')

    return app
