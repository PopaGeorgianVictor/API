
from Create_Test_MyAPI.requests.stars import *

def test_get_star_200():
    response = get_single_star(1)
    assert response.status_code == 200, 'my star is not available'
