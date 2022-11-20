from fastapi import APIRouter, Query
from .models import CasoMedicoResponse

router = APIRouter()


@router.get("/",
            response_model=list[CasoMedicoResponse],
            response_model_exclude_unset=True)
async def casos_medicos(
    especialidad: str | None = Query(
        default=None, min_length=3, max_length=50),
):
    """
    Endpoint para la busqueda de casos medicos
    """
    # TODO filtrar los datos
    results = [{"especialidad": especialidad}]
    return results
