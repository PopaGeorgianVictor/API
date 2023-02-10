import requests

def patch_order(customer_name, orderid, token):
    request_body = {
        "customerName": {customer_name}
    }

    header_params = {'Authorization': token}
    response = requests.patch(f"https://simple-books-api.glitch.me/orders/{orderid}", json=request_body, headers=header_params)
    return response
