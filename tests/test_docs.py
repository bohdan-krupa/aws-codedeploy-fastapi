import requests


def test_docs():
    response = requests.get("http://localhost:8000/docs")
    assert response.status_code == 200
