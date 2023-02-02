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
    file = open('../TestCases/AddUser.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(APP_URL,request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    tech_api_url = "https://thetestingworldapi.com/api/technicalskills"
    file = open('../TestCases/tehnical_skills.json', 'r')
    request_json = json.loads(file.read())
    # in the json file update id and st_id
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    address_api_url = "https://thetestingworldapi.com/api/addresses"
    file = open('../TestCases/address.json', 'r')
    request_json = json.loads(file.read())
    request_json['stId'] = id[0]
    response = requests.post(address_api_url, request_json)
    print(response.text)

    finals_details = "https://thetestingworldapi.com/api/FinalStudentDetails/" + str(id[0])
    response = requests.get(finals_details)
    print(response.text)