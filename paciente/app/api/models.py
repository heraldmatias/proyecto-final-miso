from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PacienteResponse(BaseModel):
    """
    Representa los datos públicos de una paciente
    """
    id: str | None
    nombres: str | None
    ubicacion: str | None
    ciudad: str | None
    pais: str | None
