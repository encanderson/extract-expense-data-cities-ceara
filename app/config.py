from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    MONGO_DB_URL: str = os.getenv('MONGO_DB_URL')
    URI_TCM: str = os.getenv('URI_TCM')

    class Config:
        case_sensitive = True


settings = Settings()
