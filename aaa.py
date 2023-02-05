
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
assert  response.status_code == 200 , 'Cod Invalid'

# Parse response to Json format
json_response = json.loads(response.text)
print(json_response) # return a list

# Fetch value using Json Path
pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages)
assert pages[0] == 2 ,'numarul nu este corect' # fetching the first value of the list