from fastapi import Response, status
import requests
from ..services.config import Settings


def buscar_pacientes_por_casos_medicos(
    response: Response,
    settings: Settings,
    medico_id: int,
    skip: int = 1,
    limit: int = 20,
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

        query = f"?tipo_lesion={medico['especialidad']}&skip={skip}&limit={limit}"

        casos_response = requests.get(
            f"{settings.code_medico_host}/casos-medicos/{query}",
            timeout=settings.request_timeout
        )
        casos_response.raise_for_status()
        casos = casos_response.json()

        paciente_id = casos[0]["paciente_id"]

        paciente_response = requests.get(
            f"{settings.pacientes_host}/pacientes/{paciente_id}/",
            timeout=settings.request_timeout
        )
        paciente_response.raise_for_status()
        paciente = paciente_response.json()

        return list(map(lambda item: {**item, **paciente}, casos))
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return [{"error": "Servicio no disponible intente nuevamente."}]
