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


@pytest.fixture
def user_for_update():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        f"https://reqres.in/api/users/",
        json=body,
        headers=headers
    )

    assert response.status_code == 201, f'Expected Status Code 201, but got {response.status_code}'
    user_data = response.json()
    yield user_data

    delete_response = requests.delete(
        f'https://reqres.in/api/users/{user_data["id"]}',
        headers=headers
    )
    assert delete_response.status_code == 204, f'Expected Status Code 204, but got {delete_response.status_code}'