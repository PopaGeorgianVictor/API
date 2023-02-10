import requests

def delete_order(orderId, token):
    header_params = {'Authorization': token}
    response = requests.delete(f"https://simple-books-api.glitch.me/orders/{orderId}", headers=header_params)
    return response
