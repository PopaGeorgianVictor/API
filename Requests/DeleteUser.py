
''' 1. Delete Resorce
    2. Use delete method of API
'''

import requests

# API URL
url = "https://reqres.in/api/users/2"

response = requests.delete(url)
print(response) # get 204

# Fetch Response Code
print(response.status_code) # get 204
assert response.status_code == 204, "API Error"