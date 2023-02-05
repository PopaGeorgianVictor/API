import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"

def test_create_new_user():
    file = open("./CreateUser.json", 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201 , 'status code nu este corect'
    response_json = json.loads(response.text)
    name = jsonpath.jsonpath(response_json, 'name')
    assert name[0] == 'George' , 'numele nu este corect'
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])
