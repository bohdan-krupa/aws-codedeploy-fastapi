import requests


def test_docs():
    response = requests.get("http://localhost/docs")
    assert response.status_code == 200
