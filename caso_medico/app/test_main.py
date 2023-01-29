from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/casos-medicos")
    assert response.status_code == 200
    assert len(response.json()) > 0
