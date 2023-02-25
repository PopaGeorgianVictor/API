
from Create_Test_MyAPI.requests.stars import *

def test_get_my_star():
    response = get_single_star(1)
    assert response.status_code == 200, 'my star is not available'

def test_get_star_id():
    response = get_single_star(3)
    assert response.json()['id'] == 3, 'is not my star id'

def test_get_star_email():
    response = get_single_star(2)
    assert response.json()['email'] == 'mila.kunis@gmail.com', 'is not my star email'

def test_get_star_first_name():
    response = get_single_star(4)
    assert response.json()['first_name'] == 'Louis', 'is not my first_name star'

def test_get_star_last_name():
    response = get_single_star(5)
    assert response.json()['last_name'] == 'Radulescu', 'is not my last_name star'

def test_get_star_avatar():
    response = get_single_star(6)
    assert response.json()['avatar'] == 'https://deadline.com/wp-content/uploads/2022/12/Celine-Dion.jpg', 'is not my star avatar'