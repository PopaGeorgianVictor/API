import requests

def get_single_star(star_id):
    response = requests.get(f'http://localhost:3000/stars/{star_id}')
    return response

def get_all_stars():
    response = requests.get(f'http://localhost:3000/stars')
    return response

def add_star():
    response = requests.post(f'http://localhost:3000/stars')
    return response

def update_star(star_id):
    response = requests.put(f'http://localhost:3000/stars/{star_id}')
    return response