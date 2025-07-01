import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture()
def client():
    return TestClient(app)

def test_login(client):
    response = client.post("/auth/login", data={"username": "admin", "password": "senha"})
    assert response.status_code == 200
    assert "access_token" in response.json()