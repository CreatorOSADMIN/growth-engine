from fastapi.testclient import TestClient


def test_app_imports() -> None:
    from app.main import app

    assert app is not None


def test_health_returns_200(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200


def test_health_returns_json(client: TestClient) -> None:
    response = client.get("/health")
    assert response.headers["content-type"].startswith("application/json")


def test_health_indicates_healthy(client: TestClient) -> None:
    response = client.get("/health")
    assert response.json() == {"status": "ok"}
