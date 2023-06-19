from pydantic import BaseSettings, Field
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    db_connection_string: str = Field(..., env="DB_CONNECTION_STRING")
    gpt_api_key: str = Field(..., env="GPT_API_KEY")


settings = Settings()
