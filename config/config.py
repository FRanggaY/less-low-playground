from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    APP_TITLE: str = "API"
    APP_DESCRIPTION: str = "API Documentation"

    DB: str

config = Config()
