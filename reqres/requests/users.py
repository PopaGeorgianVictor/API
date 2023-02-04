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