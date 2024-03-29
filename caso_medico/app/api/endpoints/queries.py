from typing import List, Union
from app.db.crud import (
    get_paginated
)
from fastapi import APIRouter, Query, Depends
from app.api.models import CasoMedicoResponse
from app.db.database import get_db, SessionLocal
router = APIRouter()


@router.get("/",
            response_model=List[CasoMedicoResponse],
            response_model_exclude_unset=True)
async def casos_medicos(
    session: SessionLocal = Depends(get_db),
    especialidad: Union[str, None] = Query(
        default=None, min_length=3, max_length=50),
    skip: int = 0,
    limit: int = 20
):
    """
    Endpoint para la busqueda de casos medicos
    """
    casos_medicos = get_paginated(session, especialidad, skip, limit)
    return casos_medicos


@router.get("/health-check", response_model=str)
async def health_check(
    db: SessionLocal = Depends(get_db)
):
    """
    Endpoint para chequear la salud
    """
    db.execute("select 1")
    return 'ok'
