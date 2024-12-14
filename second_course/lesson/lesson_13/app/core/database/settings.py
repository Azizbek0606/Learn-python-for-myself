from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "PDP's Hotle"
    PROJECT_DESCRIPTION: str = "This is learning project"
    PROJECT_VERSION: str = "0.0.1"

