import requests

def submit_order(bookid, customer_name, token):
    request_body = {
        "bookId": {bookid},
        "customerName": {customer_name}
    }
    header_params = {'Authorization': token}
    response = requests.post("https://simple-books-api.glitch.me/orders", json=request_body, headers=header_params)
    return response
