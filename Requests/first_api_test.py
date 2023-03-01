''' 1. GET Request https://reqres.in/api/users?page=2
    2. Pick Response
    3. Display Response
'''


import requests


# API URL
url = "https://reqres.in/api/users?page=2" # https://reqres.in (base url) + /api/users?page=2 (relative url)

# Send Get Request
response = requests.get(url) # sending requests to the server
print(response) # get.py 200 response

# Display Response Content
print(response.content) # picking the content of the response (complete content)
print(response.headers) # fetch the header of the response

# Validate Status Code
assert response.status_code == 200

# Fetch Response Header
print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))

# Fetch Cookies
print(response.cookies)

# Fetch Encoding
print(response.encoding)

print(response.elapsed)

