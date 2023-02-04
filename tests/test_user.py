from API.requests import *



def test_get_user_200():
    response = get_user(1)
    assert response.status_code == 200, 'status code is not ok'


def test_get_user_id():
    response = get_user(1)
    assert response.json()['data']['id'] == 1, 'id is not ok'


def test_get_user_email():
    response = get_user(1)
    assert response.json()['data']['email'] == 'george.bluth@reqres.in', 'email is not ok'


def test_get_user_first_name():
    response = get_user(1)
    assert response.json()['data']['first_name'] == 'George', 'first name is not ok'


def test_get_user_last_name():
    response = get_user(1)
    assert response.json()['data']['last_name'] == 'Bluth', 'last name is not ok'


def test_get_user_avatar():
    response = get_user(1)
    assert response.json()['data']['avatar'] == 'https://reqres.in/img/faces/1-image.jpg', 'avatar is not ok'


def test_get_users_total():
    response = get_all_users(1)
    assert response.json()['total'] == 12, 'total nr of users is not ok'


def test_get_users_totals():
    response = get_all_users(1)
    expected_user = {
        'id': 1,
        'email': 'george.bluth@reqres.in',
        'first_name': 'George',
        'last_name': 'Bluth',
        'avatar': 'https://reqres.in/img/faces/1-image.jpg'
    }
    assert response.json()['data'][0] == expected_user, 'user data is not ok'


def test_add_user():
    response = add_user('Andy', 'trainer')
    assert 'id' in response.json().keys(), 'user not created'