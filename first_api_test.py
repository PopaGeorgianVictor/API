import requests


# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)
print(response)

# Display Response Content
print(response.content)
print()
print(response.headers)
