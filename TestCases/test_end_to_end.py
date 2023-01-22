'''
1. Add New Student
2. Add Tehnical Skills
3. Add Address
4. Fetch Complete details
'''

import requests
import json
import jsonpath


def test_Add_new_data():
    APP_URL = "https://thetestingworldapi.com/api/studentsDetails"
    file = open('D:\\selenium project\\API\\TestCases\\AddUser.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(APP_URL,request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    tech_api_url = "https://thetestingworldapi.com/api/technicalskills"
    file = open('D:\\selenium project\\API\\TestCases\\tehnical_skills.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(tech_api_url, request_json)
    print(response.text)