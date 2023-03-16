import requests

def get_all_books(type="",limit=""):
    if type == "" and limit == "":
        response = requests.get("https://simple-books-api.glitch.me/books")
    elif type != "" and limit == "":
        response = requests.get(f"https://simple-books-api.glitch.me/books?type={type}")
    elif type == "" and limit != "":
        response = requests.get(f"https://simple-books-api.glitch.me/books?limit={limit}")
    else:
        response = requests.get(f"https://simple-books-api.glitch.me/books?limit={limit}&type={type}")
    return response

