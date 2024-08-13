import requests
import pytest


@pytest.fixture
def login():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post('https://reqres.in/api/login', json=body)
    assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'
    yield response.json()['token']
