from fastapi import APIRouter, Query, Depends, Response
from .models import BusquedaPacienteResponse
from ..services.config import Settings, get_settings
from . import aggregator

router = APIRouter()


@router.get("/",
            response_model=list[BusquedaPacienteResponse],
            response_model_exclude_unset=True)
async def busqueda_paciente(
    response: Response,
    settings: Settings = Depends(get_settings),
    medico_id: int = Query(gt=0),
    skip: int = 1,
    limit: int = 20
):
    """
    Endpoint para la busqueda de paciente según su caso médico
    """
    results = aggregator.buscar_pacientes_por_casos_medicos(
        response=response,
        settings=settings,
        medico_id=medico_id,
        skip=skip,
        limit=limit,
    )
    return results


@router.get("/health-check", response_model=str)
async def health_check(
    # db: Session = Depends(get_db)
):
    """
    Endpoint para chequear la salud
    """
    # db.execute("select 1")
    return 'ok'
