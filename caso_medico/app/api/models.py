from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CasoMedicoResponse(BaseModel):
    """
    Representa los datos públicos de un caso medico
    """
    id: str
    paciente_id: str
    tipo_lesion: str
    forma_lesion: str
    descripcion: str
    especialidad: str

    class Config:
        orm_mode = True
