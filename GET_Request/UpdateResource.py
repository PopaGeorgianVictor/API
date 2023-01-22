'''
PUT it use for updating resource on server

1. Read Updated json from file
2. Parse into json format
3. Hit Put method
4. Parse response to Json format
5. Validate Response
'''

import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users/2"

# Read input json from file
file = open("C:\\Users\\popag\\OneDrive\\Desktop\\DOC\\API\\CreateUserJsonUpdate.json", 'r')
'''1. create json file for updating data
   2. updating to double \ ( sigle \ - wprks like escape character)
   3. mode to be open : read only mode'''

json_input = file.read() # read complete content of the file, just a string

# Parse data into json format
request_json = json.loads(json_input)

# Make PUT request with Json Input body
response = requests.put(url,request_json) # giving url and data
print(response.content)

# Validating Response Code
assert response.status_code == 200

# Parse response content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li[0])