import requests

def patch_order(customer_name, orderId, token):
    request_body = {
        "customerName": {customer_name}
    }

    header_params = {'Authorization': token}
    response = requests.patch(f"https://simple-books-api.glitch.me/orders/{orderId}", json=request_body, headers=header_params)
    return response
