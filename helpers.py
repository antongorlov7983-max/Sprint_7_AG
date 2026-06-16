import requests
import random
import string
from datetime import datetime, timedelta


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def register_new_courier_and_return_login_password():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', json=payload)

    if response.status_code == 201:
        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }
    return {}

def new_order(color=None):
    if color is None:
        color = []
    date = datetime.now() + timedelta(days=2)
    form_date = date.strftime("%Y-%m-%d")
    return {
        "firstName": "Jack",
        "lastName": "Sparrow",
        "address": "The black pearl",
        "metroStation": 7,
        "phone": "+7 999 999 98 78",
        "rentTime": 2,
        "deliveryDate": form_date,
        "comment": "Saske, come back to Konoha",
        "color": color
    }
