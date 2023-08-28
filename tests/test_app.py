from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_post_movie():
    payload = {
        "title": "Superman"
    }
    response = client.post("/api/movies/recommendation", json=payload)
    assert response.status_code == 200

def test_post_nonexistent_movie_recommendation():
    payload = {
        "title": "ahbedefwrfnb7284"
    }
    response = client.post("/api/movies/recommendation",json=payload) 
    assert response.status_code == 404
