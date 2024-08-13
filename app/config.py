import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    REDIS_URL = os.getenv("CACHE_REDIS_URL")
    CACHE_TYPE = os.getenv("CACHE_TYPE")
    CACHE_REDIS_HOST = os.getenv("CACHE_REDIS_HOST")
    CACHE_REDIS_PORT = os.getenv("CACHE_REDIS_PORT")
    CACHE_REDIS_DB = os.getenv("CACHE_REDIS_DB")
    CACHE_DEFAULT_TIMEOUT = int(os.getenv("CACHE_DEFAULT_TIMEOUT"))
