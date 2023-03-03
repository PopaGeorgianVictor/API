
from IT_Factory_Project.requests.all_requests import *

class TestDelete:
    def test_delete_user(self):
        response = delete_user(11)
        assert response.status_code == 204, 'user-ul nu a fost sters'