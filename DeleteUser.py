import requests


# API URL
url = "https://reqres.in/api/users/2"

response = requests.delete(url)
print(response) # get 204

# Fetch Response Code
print(response.status_code) # get 204