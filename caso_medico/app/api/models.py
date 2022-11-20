from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CasoMedicoResponse(BaseModel):
    """
    Representa los datos públicos de un caso medico
    """
    id: str | None
    paciente_id: str | None
    tipo_lesion: str | None
    forma_lesion: str | None
    descripcion: str | None
    especialidad: str | None

    class Config:
        orm_mode = True
