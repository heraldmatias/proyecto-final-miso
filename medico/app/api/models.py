from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class MedicoResponse(BaseModel):
    """
    Representa los datos públicos de una paciente
    """
    id: str | None
    nombres: str
    especialidad: str
    ubicacion: str | None
    ciudad: str | None
    pais: str | None
