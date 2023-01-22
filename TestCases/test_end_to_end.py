'''
1. Add New Student
2. Add Tehnical Skills
3. Add Address
4. Fetch Complete details
'''

import requests
import json
import jsonpath


def test_Add_neew_data():
    APP_URL = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('D:\\selenium project\\API\\TestCases\\AddUser.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(APP_URL,request_json)
    print(response.text)
    id = jsonpath.jsonpath(request_json(),'id')