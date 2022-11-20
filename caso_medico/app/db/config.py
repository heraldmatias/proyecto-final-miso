from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    caso_medico_database_url: str


@lru_cache()
def get_settings():
    return Settings()
