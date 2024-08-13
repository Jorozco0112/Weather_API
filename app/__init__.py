import redis
from flask import Flask
from flask_caching import Cache
from .controller import weather_bp
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Flask-Caching with Redis
    cache = Cache(app=app)
    cache.init_app(app=app)

    # Register Blueprints
    app.register_blueprint(weather_bp)

    return app
