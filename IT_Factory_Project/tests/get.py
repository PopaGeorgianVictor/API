
from IT_Factory_Project.requests.all_requests import *

class TestGetUsers:
    def test_get_user(self):
        response = get_user(7)
        assert response.status_code == 200, 'status code nu este corect'

    def test_check_user_using_jsonpath(self):
        response = get_all_users(2)
        json_response = json.loads(response.text)
        user = jsonpath.jsonpath(json_response, 'data[1].last_name')
        assert user[0] == 'Ferguson', 'numele nu este corect'

    def test_get_user_id(self):
        response = get_user(7)
        assert response.json()['data']['id'] == 7, 'id-ul nu este corect'

    def test_get_user_email(self):
        response = get_user(7)
        assert response.json()['data']['email'] == 'michael.lawson@reqres.in', 'email-ul nu este corect'

    def test_get_user_first_name(self):
        response = get_user(7)
        assert response.json()['data']['first_name'] == 'Michael', 'first_name nu este corect'

    def test_get_user_last_name(self):
        response = get_user(7)
        assert response.json()['data']['last_name'] == 'Lawson', 'last_name nu este corect'

    def test_get_user_avatar(self):
        response = get_user(7)
        assert response.json()['data']['avatar'] == 'https://reqres.in/img/faces/7-image.jpg', 'avatarul nu este corect'

    def test_get_users_totals(self):
        response = get_all_users(1)
        assert response.json()['total'] == 12, 'numarul total de utilizatori nu este corect'

    def test_get_my_user(self):
        response = get_all_users(2)
        expected_user = {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        }
        assert response.json()['data'][0] == expected_user, 'datele nu sunt corecte'

    def test_user_not_found(self):
        response = get_user(70)
        assert response.status_code == 404, 'user-ul a fost gasit'

