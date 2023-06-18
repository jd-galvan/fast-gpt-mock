from pydantic import BaseSettings


class Settings(BaseSettings):
    db_connection_string: str
    gpt_api_key: str

    class Config:
        env_file = '.env'


settings = Settings()
