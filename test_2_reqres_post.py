import pytest
import requests
import allure


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('User Management')
@allure.suite('User Operations')
@allure.title('Create a new user')
@allure.description('Test the API endpoint to create a new user')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user(login):
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {login}'}

    with allure.step("Send POST request to create a new user"):
        response = requests.post(
            'https://reqres.in/api/users',
            json=body,
            headers= headers
        )

    with allure.step("Check response status code"):
        assert response.status_code == 201, f'Expected Status Code 201, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify "name" is correct'):
        assert response_data["name"] == "morpheus", f"Expected name 'morpheus', but got {response_data['name']}"

    with allure.step('Verify "job" is correct'):
        assert response_data["job"] == "leader", f"Expected job 'leader', but got {response_data['job']}"

    with allure.step('Verify response contains "id"'):
        assert "id" in response_data, "Response JSON does not contain 'id'"

    with allure.step('Verify response contains "createdAt"'):
        assert "createdAt" in response_data, "Response JSON does not contain 'createdAt'"


