from fastapi import APIRouter
from .models import PacienteResponse

router = APIRouter()


@router.get("/{paciente_id}",
            response_model=PacienteResponse,
            response_model_exclude_unset=True)
async def busqueda_paciente(
    paciente_id: int
):
    """
    Endpoint para la busqueda de pacientes
    """
    # TODO filtrar los datos
    paciente = {
        "paciente_id": paciente_id,
        "nombres": "Ivan Wenceslao Castano",
        "pais": "Colombia",
        "ciudad": "Bogota",
        "ubicacion": ""
    }
    return paciente
