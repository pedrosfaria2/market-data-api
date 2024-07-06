from fastapi.testclient import TestClient
from services.api.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Coinbase Public Data API"}


def test_get_products():
    response = client.get("/public/products")
    assert response.status_code == 200


def test_get_server_time():
    response = client.get("/public/server-time")
    assert response.status_code == 200
