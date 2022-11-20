from fastapi import APIRouter
from .models import MedicoResponse

router = APIRouter()


@router.get("/{medico_id}",
            response_model=MedicoResponse,
            response_model_exclude_unset=True)
async def obtener_medico(medico_id: int):
    """
    Endpoint para la busqueda de pacientes
    """
    results = {
        "medico_id": medico_id,
        "especialidad": "Cirugías",
        "nombres": "Mateo Correal"
    }
    return results
