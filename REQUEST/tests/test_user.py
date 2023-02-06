




from REQUEST.requests.users import *

def test_get_user_200():
    response = get_user(11)
    assert response.status_code == 200, 'status code nu este corect'

def test_get_user_id():
    response = get_user(11)
    assert response.json()['data']['id'] == 11, 'id-ul nu este corect'

def test_get_user_email():
    response = get_user(11)
    assert response.json()['data']['email'] == 'george.edwards@reqres.in', 'email-ul nu este corect'

def test_get_user_first_name():
    response = get_user(11)
    assert response.json()['data']['first_name'] == 'George', 'first_name nu este corect'

def test_get_user_last_name():
    response = get_user(11)
    assert response.json()['data']['last_name'] == 'Edwards', 'last_name nu este corect'

def test_get_user_avatar():
    response = get_user(11)
    assert response.json()['data']['avatar'] == 'https://reqres.in/img/faces/11-image.jpg', 'avatarul nu este corect'

def test_get_users_totals():
    response = get_all_users(1)
    assert response.json()['total'] == 12, 'numarul total de utilizatori nu este corect'

def test_get_my_user():
    response = get_all_users(2)
    expected_user = {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
    }
    assert response.json()['data'][4] == expected_user, 'datele nu sunt corecte'

def test_add_user():
    response = add_user('George', 'QA')
    assert 'id' in response.json().keys(), 'user-ul nu a fost creat'

