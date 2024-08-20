from flask import Flask
from .extensions import api, cache
from .controller import weather_ns
from .config import Config

def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    # Initialize the extensions
    api.init_app(app)
    cache.init_app(app)
    # Add the Weather API namespace
    api.add_namespace(weather_ns, path='/weather')

    return app
