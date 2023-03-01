
from IT_Factory_Project.requests.all_requests import *

class TestAddUser:
    def test_add_user(self):
        response = add_user('George', 'QA')
        assert response.status_code == 201, 'user-ul nu a fost creat'
        assert 'id' in response.json().keys(), 'user-ul nu a fost creat'

    def test_add_user_using_jsonfile(self):
        file = open("../tests/AddUser.json", 'r')
        json_input = file.read()
        request_json = json.loads(json_input)
        response = add_user_jsonfile(request_json)
        assert 'id' in response.json().keys(), 'user-ul nu a fost creat'
        assert response.status_code == 201, 'user-ul nu a fost creat'

    def test_register_user(self):
        response = register_user('eve.holt@reqres.in', 'pistol')
        assert response.status_code == 200, 'Register - unsuccessful'
        expected_data = {
            "id": 4,
            "token": "QpwL5tke4Pnpja7X4"
        }
        assert response.json() == expected_data, 'datele utilizatorului nu sunt corespunzatoare'

    def test_invalid_register(self):
        response = register_invalid('eve.holt@reqres.in')
        assert response.status_code == 400
        assert response.json()["error"] == "Missing password"

    def test_login(self):
        response = login_user('eve.holt@reqres.in', 'cityslicka')
        assert response.status_code == 200, 'Login - unsuccessful'
        expected_data = {
            "token": "QpwL5tke4Pnpja7X4"
        }
        assert response.json() == expected_data, 'datele utilizatorului nu sunt corespunzatoare'

    def test_invalid_login(self):
        response = login_invalid('peter@klaven')
        assert response.status_code == 400
        assert response.json()["error"] == "Missing password"