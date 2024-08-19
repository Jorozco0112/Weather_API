from flask_restx import Api
from flask_caching import Cache

# Initialize Flask-RESTx
api = Api(
    version="1.0",
    title="Weather API",
    description="A simple Weather API with caching",
)

cache = Cache()  # Initialize Cache
