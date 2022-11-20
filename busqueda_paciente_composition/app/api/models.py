from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BusquedaPacienteResponse(BaseModel):
    """
    Representa el response de busqueda de paciente, se enviará una lista
    donde cada elemento tendrá la estructura definida en esta clase.
    """
    nombre_paciente: str | None
    tipo_lesion: str | None
    caso_medico_id: str | None
    ubicacion: str | None
    ciudad: str | None
    pais: str | None
    error: str | None
