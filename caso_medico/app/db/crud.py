from typing import List
from .database import SessionLocal
from .models import CasoMedico


def get_paginated(
    db_session: SessionLocal, especialidad: str, skip=0, limit=100
) -> List[CasoMedico]:
    query = db_session.query(CasoMedico).offset(skip)
    if limit:
        query = query.limit(limit)
    return query.all()
