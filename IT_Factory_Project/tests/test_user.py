
from IT_Factory_Project.requests.users import *

def test_get_user_200():
    response = get_user(7)
    assert response.status_code == 200, 'status code nu este corect'

def test_get_user_id():
    response = get_user(7)
    assert response.json()['data']['id'] == 7, 'id-ul nu este corect'

def test_get_user_email():
    response = get_user(7)
    assert response.json()['data']['email'] == 'michael.lawson@reqres.in', 'email-ul nu este corect'

def test_get_user_first_name():
    response = get_user(7)
    assert response.json()['data']['first_name'] == 'Michael', 'first_name nu este corect'

def test_get_user_last_name():
    response = get_user(7)
    assert response.json()['data']['last_name'] == 'Lawson', 'last_name nu este corect'

def test_get_user_avatar():
    response = get_user(7)
    assert response.json()['data']['avatar'] == 'https://reqres.in/img/faces/7-image.jpg', 'avatarul nu este corect'

def test_get_users_totals():
    response = get_all_users(1)
    assert response.json()['total'] == 12, 'numarul total de utilizatori nu este corect'

def test_get_my_user():
    response = get_all_users(2)
    expected_user = {
        "id": 7,
        "email": "michael.lawson@reqres.in",
        "first_name": "Michael",
        "last_name": "Lawson",
        "avatar": "https://reqres.in/img/faces/7-image.jpg"
    }
    assert response.json()['data'][0] == expected_user, 'datele nu sunt corecte'

def test_add_user():
    response = add_user('George', 'QA')
    assert 'id' in response.json().keys(), 'user-ul nu a fost creat'

def test_update_data_user():
    response = update_user_data(46,'Georgian', 'SUPER QA')
    assert response.status_code == 200 , 'informatiile nu au fost actualizate'

def test_delete_user():
    response = delete_user(11)
    assert response.status_code == 204, 'user-ul nu a fost sters'

def test_user_not_found():
    response = get_user(70)
    assert response.status_code == 404, 'user-ul a fost gasit'

def test_register_user():
    response = register_user('eve.holt@reqres.in','pistol')
    assert response.status_code == 200 , 'Register - unsuccessful'
    expected_data = {
    "id": 4,
    "token": "QpwL5tke4Pnpja7X4"
}
    assert response.json() == expected_data, 'datele utilizatorului nu sunt corespunzatoare'

def test_login():
    response = login_user('eve.holt@reqres.in', 'cityslicka')
    assert response.status_code == 200, 'Login - unsuccessful'
    expected_data = {
        "token": "QpwL5tke4Pnpja7X4"
    }
    assert response.json() == expected_data, 'datele utilizatorului nu sunt corespunzatoare'