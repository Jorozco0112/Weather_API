from flask_restx import Api

# Initialize Flask-RESTx
api = Api(
    version="1.0",
    title="Weather API",
    description="A simple Weather API with caching",
)
