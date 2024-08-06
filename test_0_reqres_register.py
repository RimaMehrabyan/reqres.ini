import pytest
import requests
import allure


@allure.feature('User Management')
@allure.suite('User Operations')
@allure.title('Register a new user successfully')
@allure.description('Test the API endpoint for successful user registration')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_register_successful():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step("Send POST request to register a new user"):
        response = requests.post(
            'https://reqres.in/api/register',
            json=body,
            headers=headers
        )

    with allure.step("Check response status code"):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains "id"'):
        assert "id" in response_data, "Response JSON does not contain 'id'"

    with allure.step('Verify "id" is correct'):
        assert response_data["id"] == 4, f"Expected ID 4, but got {response_data['id']}"

    with allure.step('Verify response contains "token"'):
        assert "token" in response_data, "Response JSON does not contain 'token'"

    with allure.step('Verify "token" is correct'):
        assert response_data["token"] == "QpwL5tke4Pnpja7X4", f"Expected token 'QpwL5tke4Pnpja7X4', but got {response_data['token']}"


@allure.feature('User Management')
@allure.suite('User Operations')
@allure.title('Unsuccessful user registration')
@allure.description('Test the API endpoint for unsuccessful user registration')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_register_unsuccessful():
    body = {
        "email": "sydney@fife"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step("Send POST request to register a new user with missing password"):
        response = requests.post(
            'https://reqres.in/api/register',
            json=body,
            headers=headers
        )

    with allure.step("Check response status code"):
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains "error"'):
        assert "error" in response_data, "Response JSON does not contain 'error'"

    with allure.step('Verify "error" is correct'):
        assert response_data["error"] == "Missing password", f"Expected error 'Missing password', but got {response_data['error']}"