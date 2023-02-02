'''
1. Convert TestCase into Pytest format
2. Execute TestCase using Python
3. Write Multiple TestCase in a File
'''

import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"

def test_create_new_user():
    # Read input json from file
    file = open("../TestCases/NewUser.json", 'r')
    json_input = file.read()  # read complete content of the file, just a string
    request_json = json.loads(json_input)
    print(request_json)  # checking if I am able to read and pars into json format
    # Make POST request with Json Input body
    response = requests.post(url, request_json)  # giving url and data
    print(response.content)
    # Validating Response Code
    assert response.status_code == 201


def test_create_other_user():
    # Read input json from file
    file = open("../TestCases/AddUser.json", 'r')
    json_input = file.read()  # read complete content of the file, just a string
    request_json = json.loads(json_input)
    # Make POST request with Json Input body
    response = requests.post(url, request_json)  # giving url and data
    print(response.content)
    response_json = json.loads(response.text)
    # Pick Id using Json Path (fetch first item in the list)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])  # getting a new id every time I running because a new resource is created