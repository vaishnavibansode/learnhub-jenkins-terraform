import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.app import app


def test_homepage():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"LearnHub" in response.data
    assert b"Python Programming" in response.data


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "application": "LearnHub Online Learning Platform",
        "status": "healthy"
    }


def test_invalid_route():
    client = app.test_client()
    response = client.get("/invalid-route")

    assert response.status_code == 404
