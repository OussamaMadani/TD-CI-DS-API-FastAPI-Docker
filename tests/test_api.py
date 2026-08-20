from fastapi.testclient import TestClient

from app.main import app


def test_read_root():
    with TestClient(app) as client:
        response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "API is intentionally broken!"}


def test_predict():
    with TestClient(app) as client:
        response = client.post("/predict", json={"features": [1.0, 2.0, 3.0]})

    assert response.status_code == 200
    assert response.json()["predictions"] == [2.0, 4.0, 6.0]


def test_predict_rejects_invalid_payload():
    with TestClient(app) as client:
        response = client.post("/predict", json={"features": "invalid"})

    assert response.status_code == 422
