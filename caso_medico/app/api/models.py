from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CasoMedicoResponse(BaseModel):
    """
    Representa los datos públicos de un caso medico
    """
    id: str | None
    id_paciente: str | None
    tipo_lesion: str | None
    forma: str | None
    descripcion: str | None
    especialidad: str | None
