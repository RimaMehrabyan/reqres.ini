import pytest
import requests
import allure


@allure.feature('User Management')
@allure.suite('User Operations')
@allure.title('Update user details')
@allure.description('Test the API endpoint to update details of an existing user')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_update(user_for_update):
    user_id = user_for_update["id"]
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step(f"Send PUT request to update details of user with ID {user_id}"):
        response = requests.put(
            f'https://reqres.in/api/users/{user_id}',
            json=body,
            headers=headers
        )

    with allure.step("Check response status code"):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step("Check if the response contains the updated name"):
        assert response_data["name"] == "morpheus", f"Expected name 'morpheus', but got {response_data['name']}"

    with allure.step("Check if the response contains the updated job"):
        assert response_data["job"] == "zion resident", f"Expected job 'zion resident', but got {response_data['job']}"

    with allure.step("Check if the response contains 'updatedAt' timestamp"):
        assert "updatedAt" in response_data, "Response JSON does not contain 'updatedAt'"

