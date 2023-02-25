import requests

def get_single_star(star_id):
    response = requests.get(f'http://localhost:3000/stars/{star_id}')
    return response

def get_all_stars():
    response = requests.get(f'http://localhost:3000/stars')
    return response

def add_star(email,first_name,last_name,avatar):
    new_star = {
        'email' : email,
        'first_name' :first_name,
        'last_name' : last_name,
        'avatar' : avatar
    }
    response = requests.post(f'http://localhost:3000/stars', new_star)
    return response

def update_star(star_id):
    update_star = {
        'email' : email,
        'first_name' :first_name,
        'last_name' : last_name,
        'avatar' : avatar
    }
    response = requests.put(f'http://localhost:3000/stars/{star_id}', update_star)
    return response

def delete_star(star_id):
    response = requests.delete(f'http://localhost:3000/stars/{star_id}')
    return response