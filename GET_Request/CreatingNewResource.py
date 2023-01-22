'''
POST method it use for creating a new resource on the server
PUT use for updating data

STEPS

1. Read input json from file (create a json file in notepad++)
2. Parse into json format
3. Hit post method
4. Parse response to json format
5. Validate response
'''

import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"

# Read input json from file
file = open("C:\\Users\\popag\\OneDrive\\Desktop\\DOC\\API\\CreateUserJson.json", 'r')
'''1. create json file
   2. updating to double \ ( sigle \ - wprks like escape ckaracter)
   3. mode to be open : read only mode'''

json_input = file.read() # read complete content of the file, just a string

# Parse data into json format
request_json = json.loads(json_input)
print(request_json) # checking if I am able to read and pars into json format

# Make POST request with Json Input body
response = requests.post(url,request_json) # giving url and data
print(response.content)

# Validating Response Code
assert response.status_code == 201

# Fetch Header from Response
print(response.headers)
print(response.headers.get('Content-Length'))

# Parse response to json format
response_json = json.loads(response.text)

# Pick Id using Json Path (fetch first item in the list id[0])
id = jsonpath.jsonpath(response_json, 'id')
print(id[0]) # getting a new id every time I running because a new resource is created

