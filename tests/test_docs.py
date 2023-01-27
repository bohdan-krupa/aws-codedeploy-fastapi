import requests


def test_docs():
    response = requests.get("http://127.0.0.1/docs")
    assert response.status_code == 200
