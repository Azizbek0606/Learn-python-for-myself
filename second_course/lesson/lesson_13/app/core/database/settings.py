from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME = str
    PROJECT_DESCRIPTION = str