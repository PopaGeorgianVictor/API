
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

def test_check_my_star():
    response = get_all_stars()
    expected_star = {
        "id" : 1,
        "email": "popa.georgian93@gamil.com",
        "first_name": "Georgian",
        "last_name": "Popa",
        "avatar": "https://npg.si.edu/sites/default/files/styles/grid_wider/public/promotion/npg-npg_87_43.jpg?itok=pWuMxYem"
    }

    assert response.json()[0] == expected_star, 'my details star is not gorgeous'


def test_add_new_star():
    response = add_star('rowan.atkinson@gmail.com','Rowan','Atkinson','https://s3-eu-central-1.amazonaws.com/cartoons-s3/styles/product_detail_image/s3/A1933644-9BF6-4911-84EB-63714057C628.jpeg?itok=6bfdu737')
    assert 'id' in response.json().keys()

def test_update_star():
    response =

def test_delete_star():
    response = delete_star(7)
    assert response.status_code == 204, 'star is forever'