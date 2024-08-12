import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    API_KEY = os.getenv("API_KEY")
    REDIS_URL = os.getenv("REDIS_URL")
    CACHE_TYPE = os.getenv("CACHE_TYPE")
    CACHE_REDIS_HOST = os.getenv("CACHE_REDIS_HOST")
    CACHE_REDIS_PORT = os.getenv("CACHE_REDIS_PORT")
    CACHE_REDIS_DB = os.getenv("CACHE_REDIS_DB")
