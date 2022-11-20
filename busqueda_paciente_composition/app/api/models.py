from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BusquedaPacienteResponse(BaseModel):
    """
    Representa el response de busqueda de paciente, se enviará una lista
    donde cada elemento tendrá la estructura definida en esta clase.
    """
    nombres: str | None
    tipo_lesion: str | None
    forma_lesion: str | None
    descripcion: str | None
    ubicacion: str | None
    ciudad: str | None
    pais: str | None
    error: str | None
