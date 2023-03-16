from IT_Factory_Project.requests.all_requests import *

class TestUpdateUser:
    def test_update_data_user(self):
        response = update_user_data(46,'Georgian', 'SUPER QA')
        assert response.status_code == 200 , 'informatiile nu au fost actualizate'