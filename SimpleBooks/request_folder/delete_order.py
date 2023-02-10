import requests
from requests_folder.get_token import generate_token

def delete_order(orderId):
    header_params = {'Authorization': token}
    response = requests.delete(f"https://simple-books-api.glitch.me/orders/{orderId}", headers=header_params)
    return response
