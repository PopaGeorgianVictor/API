'''
POST method it use for creating a new resource on the server

STEPS

1. Read input json from file (create a json file in notepad++)
2. Parse into json format
3. Hit post method
4. Parse response to json format
5. Validate response
'''

import requests

# API URL
url = "https://reqres.in/api/users"


# Read input json from file
file = open("C:\\Users\\popag\\OneDrive\\Desktop\\DOC\\API\\CreateUserJson.json", 'r')
# updating to double \
# mode to be open : read mode

json_input = file.read() # read complete content of the file