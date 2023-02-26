
import requests

def get_user(user_id):
    response = requests.get(f'https://reqres.in/api/users/{user_id}')
    return response

def get_all_users(page):
    response = requests.get(f'https://reqres.in/api/users?page={page}')
    return response

def add_user(name, job):
    data = {
        'name': name,
        'job': job
    }
    response = requests.post(f'https://reqres.in/api/users', data)
    return response

def update_user_data(name, job,user_id):
    update_data = {
        'name': name,
        'job': job
    }
    response = requests.put(f'https://reqres.in/api/users/{user_id}', update_data)
    return response

def delete_user(user_id):
    response = requests.delete(f'https://reqres.in/api/users/{user_id}')
    return response

def register_user(email,password):
    register_user = {
        "email": email,
        "password": password }

    response = requests.post('https://reqres.in/api/register', register_user)
    return response

def register_invalid(email):
    register_invalid = {
        "email": email}

    response = requests.post('https://reqres.in/api/register', register_invalid)
    return response


def login_user(email,password):
    login_user = {
        "email": email,
        "password": password }

    response = requests.post('https://reqres.in/api/login', login_user)
    return response