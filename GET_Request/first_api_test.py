import requests

''' 1. GET Request https://reqres.in/api/users?page=2
    2. Pick Response
    3. Display Response
'''

# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url) # sending request to the server
print(response) # get 200 response

# Display Response Content
print(response.content) # picking the content of the response
print(response.headers) # fetch the header of the response
