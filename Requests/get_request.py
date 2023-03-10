
''' FETCH sau GET
    1. Fetch Response Content
    2. Json Path '''
import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# Get Request
response = requests.get(url)
assert  response.status_code == 200 , 'status cod invalid'

# Parse response to Json format
json_response = json.loads(response.text)
print(json_response)

# Fetch value using Json Path
users = jsonpath.jsonpath(json_response,'total')
assert users[0] == 12 ,'numarul de utilizatori nu este corect'
user = jsonpath.jsonpath(json_response,'data[1].last_name')
assert user[0] == 'Ferguson' , 'numele nu este corect'

for nume in json_response['data']:
    print(nume['first_name'])