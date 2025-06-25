from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_account():
    response = client.post("/accounts/", json={"name": "Teste", "balance": 100})
    assert response.status_code == 201

def test_get_accounts():
    response = client.get("/accounts/")
    assert response.status_code == 200

def test_summary_report():
    response = client.get("/reports/summary")
    assert response.status_code == 200
    assert "total_income" in response.json()
