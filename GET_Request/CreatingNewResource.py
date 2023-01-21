'''
POST method it use for creating a new resource on the server

STEPS

1. Read input json from file
2. Parse into json format
3. Hit post method
4. Parse response to json format
5. Validate response
'''

import requests

# API URL
url = "https://reqres.in/api/users"
