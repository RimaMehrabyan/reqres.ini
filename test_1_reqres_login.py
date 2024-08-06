import pytest
import requests
import allure


@allure.feature('User Management')
@allure.suite('User Operations')
@allure.title('Successful user login')
@allure.description('Test the API endpoint for successful user login')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_login_successful():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step("Send POST request for user login"):
        response = requests.post(
            'https://reqres.in/api/login',
            json=body,
            headers=headers
        )

    with allure.step("Check response status code"):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains "token"'):
        assert "token" in response_data, "Response JSON does not contain 'token'"

    with allure.step('Verify "token" is correct'):
        assert response_data["token"] == "QpwL5tke4Pnpja7X4", f"Expected token 'QpwL5tke4Pnpja7X4', but got {response_data['token']}"


@allure.feature('User Management')
@allure.suite('User Operations')
@allure.title('Unsuccessful user login')
@allure.description('Test the API endpoint for unsuccessful user login')
@pytest.mark.regression
def test_login_unsuccessful():
    body = {
        "email": "peter@klaven"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step("Send POST request for user login with missing password"):
        response = requests.post(
            'https://reqres.in/api/login',
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