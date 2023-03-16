
''' FETCH or GET
    1. Fetch Response Content
    2. Json Path '''

import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)


# Parse response to Json format
json_response = json.loads(response.text)
print(json_response)# return a list

# Fetch value using Json Path
pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])
assert pages[0] == 2 , 'API Error' # fetching the first value of the list
user = jsonpath.jsonpath(json_response,'data[1].last_name')
print(user[0])
assert user[0] == 'Ferguson'

for val in json_response['data']:
    print(val['first_name'])