import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret-key")
    DATABASE_URL: str = "sqlite:///./tunzaa.db"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()