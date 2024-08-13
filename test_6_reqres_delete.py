import pytest
import requests
import allure


@allure.feature('User Management')
@allure.suite('User Operations')
@allure.title('Delete user')
@allure.description('Test the API endpoint to delete an existing user')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_delete():
    headers = {'Content-Type': 'application/json'}

    with allure.step(f"Send DELETE request to remove user with ID 2"):
        response = requests.delete(
            f'https://reqres.in/api/users/2',
            headers=headers
        )

    with allure.step("Check response status code"):
        assert response.status_code == 204, f'Expected Status Code 204, but got {response.status_code}'