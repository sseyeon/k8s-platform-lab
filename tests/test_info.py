from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_application_info():
    response = client.get("/api/info")

    data = response.json()

    assert response.status_code == 200
    assert data["application"] == "k8s-platform-lab"
    assert data["version"] == "1.0.0"
    assert data["environment"] == "local"
    assert "hostname" in data