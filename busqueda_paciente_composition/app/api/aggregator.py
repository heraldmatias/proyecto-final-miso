from fastapi import Response, status
import requests
from ..services.config import Settings


def buscar_pacientes_por_casos_medicos(
    response: Response,
    settings: Settings,
    medico_id: int,
    per_page: int = 20,
    page: int = 1,
):
    """
    Agregador que busca pacientes
    """
    try:
        medico_response = requests.get(
            f"{settings.medico_host}/medicos/{medico_id}/",
            timeout=settings.request_timeout
        )
        medico_response.raise_for_status()
        medico = medico_response.json()

        query = f"?tipo_lesion={medico['especialidad']}&per_page={per_page}&page={page}"

        casos = requests.get(f"{settings.code_medico_host}/casos-medicos/{query}",
                             timeout=settings.request_timeout)

        results = [{"tipo_lesion": "tipo_lesion"}]

        return results
    except requests.exceptions.HTTPError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return [{"error": "Servicio no disponible intente nuevamente en algunos minutos."}]
