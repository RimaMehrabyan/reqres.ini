import requests
import pytest
import allure


@allure.feature('User Management')
@allure.suite('User Operations')
@allure.title('List users on page 2')
@allure.description('Test the API endpoint to list users on page 2')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_list_users():
    with allure.step("Send GET request to list users on page 2"):
        response = requests.get('https://reqres.in/api/users?page=2')

    with allure.step("Check response status code"):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    response_data = response.json()

    with allure.step("Check if 'page' is in response JSON"):
        assert "page" in response_data, "Response JSON does not contain 'page'"

    with allure.step("Check if the page is 2"):
        assert response_data["page"] == 2, f"Expected page 2, but got {response_data['page']}"

    with allure.step("Check if 'data' is in response JSON"):
        assert "data" in response_data, "Response JSON does not contain 'data'"

    with allure.step("Check if there are 6 users"):
        assert len(response_data["data"]) == 6, f"Expected 6 users, but got {len(response_data['data'])}"

    for user in response_data["data"]:
        with allure.step("Check if 'id' is present"):
            assert "id" in user, "User JSON does not contain 'id'"

        with allure.step("Check if 'email' is present"):
            assert "email" in user, "User JSON does not contain 'email'"

        with allure.step("Check if 'first_name' is present"):
            assert "first_name" in user, "User JSON does not contain 'first_name'"

        with allure.step("Check if 'last_name' is present"):
            assert "last_name" in user, "User JSON does not contain 'last_name'"

        with allure.step("Check if 'avatar' is present"):
            assert "avatar" in user, "User JSON does not contain 'avatar'"

    with allure.step("Check if 'support' is in response JSON"):
        assert "support" in response_data, "Response JSON does not contain 'support'"

    with allure.step("Check if 'url' is in support JSON"):
        assert "url" in response_data["support"], "Support JSON does not contain 'url'"

    with allure.step("Check if 'text' is in support JSON"):
        assert "text" in response_data["support"], "Support JSON does not contain 'text'"


@allure.feature('User Management')
@allure.suite('User Operations')
@allure.title('Get single user details')
@allure.description('Test the API endpoint to get details of a single user with ID 2')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_single_user():
    with allure.step("Send GET request to get details of user with ID 2"):
        response = requests.get('https://reqres.in/api/users/2')

    with allure.step("Check response status code"):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    response_data = response.json()

    with allure.step("Check if 'data' is in response JSON"):
        assert "data" in response_data, "Response JSON does not contain 'data'"

    user = response_data["data"]

    with allure.step("Check user ID"):
        assert user["id"] == 2, f"Expected user ID 2, but got {user['id']}"

    with allure.step("Check user email"):
        assert user["email"] == "janet.weaver@reqres.in", f"Expected email 'janet.weaver@reqres.in', but got {user['email']}"

    with allure.step("Check user first name"):
        assert user["first_name"] == "Janet", f"Expected first name 'Janet', but got {user['first_name']}"

    with allure.step("Check user last name"):
        assert user["last_name"] == "Weaver", f"Expected last name 'Weaver', but got {user['last_name']}"

    with allure.step("Check user avatar URL"):
        assert user["avatar"] == "https://reqres.in/img/faces/2-image.jpg", f"Expected avatar URL 'https://reqres.in/img/faces/2-image.jpg', but got {user['avatar']}"


    with allure.step("Check if 'support' is in response JSON"):
        assert "support" in response_data, "Response JSON does not contain 'support'"

    with allure.step("Check support URL"):
        assert response_data["support"]["url"] == "https://reqres.in/#support-heading", f"Expected support URL 'https://reqres.in/#support-heading', but got {response_data['support']['url']}"

    with allure.step("Check support text"):
        assert response_data["support"]["text"] == "To keep ReqRes free, contributions towards server costs are appreciated!", f"Expected support text, but got {response_data['support']['text']}"


@allure.feature('User Management')
@allure.suite('User Operations')
@allure.title('User not found')
@allure.description('Test the API endpoint to get details of a non-existent user with ID 23')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_user_not_found():
    with allure.step("Send GET request to get details of a non-existent user with ID 23"):
        response = requests.get('https://reqres.in/api/users/23')

    with allure.step("Check response status code"):
        assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

    response_data = response.json()

    with allure.step("Check if response JSON is empty"):
        assert response_data == {}, f"Expected empty JSON response, but got {response_data}"




