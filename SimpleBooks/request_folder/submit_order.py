import requests

def submit_order(bookId, customer_name, token):
    request_body = {
        "bookId": {bookId},
        "customerName": {customer_name}
    }
    header_params = {'Authorization': token}
    response = requests.post("https://simple-books-api.glitch.me/orders", json=request_body, headers=header_params)
    return response
