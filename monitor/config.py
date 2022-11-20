from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    pacientes_host: str = "http://localhost:8000"
    caso_medico_host: str = "http://localhost:8002"
    medico_host: str = "http://localhost:8001"
    busqueda_pacientes_host: str = "http://localhost:8004"
    request_timeout: int = 5
    servicios: list[dict] = [
        {
            "name": "Pacientes",
            "url": f"{pacientes_host}/pacientes/health-check"
        },
        {
            "name": "Caso Medico",
            "url": f"{caso_medico_host}/casos-medicos/health-check"
        },
        {
            "name": "Medicos",
            "url": f"{medico_host}/medicos/health-check"
        },
        {
            "name": "Busqueda Pacientes",
            "url": f"{busqueda_pacientes_host}/consulta-pacientes/health-check"
        }
    ]


@lru_cache()
def get_settings():
    return Settings()
