import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlmodel import SQLModel
from app.database import engine

@pytest.fixture(scope="module")
def test_db():
    SQLModel.metadata.create_all(bind=engine)
    yield
    SQLModel.metadata.drop_all(bind=engine)

@pytest.fixture()
def client():
    return TestClient(app)

def test_get_transactions(client):
    response = client.get("/transactions/")
    assert response.status_code == 200
