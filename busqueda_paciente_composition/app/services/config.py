from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    pacientes_host: str = "http://localhost:8000"
    code_medico_host: str = "http://localhost:8002"
    medico_host: str = "http://localhost:8001"
    request_timeout: int = 2


@lru_cache()
def get_settings():
    return Settings()
