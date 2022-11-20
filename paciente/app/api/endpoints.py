from fastapi import APIRouter, Query
from .models import PacienteResponse

router = APIRouter()


@router.get("/",
            response_model=list[PacienteResponse],
            response_model_exclude_unset=True)
async def busqueda_paciente(
    nombre_paciente: str | None = Query(
        default=None, min_length=3, max_length=50),
    pais: str | None = Query(
        default=None, min_length=3, max_length=50),
    ciudad: str | None = Query(
        default=None, min_length=3, max_length=50),
):
    """
    Endpoint para la busqueda de pacientes
    """
    # TODO filtrar los datos
    results = [{"nombre_paciente": nombre_paciente,
                "pais": pais, "ciudad": ciudad}]
    return results
