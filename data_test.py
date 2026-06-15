from helpers import generate_random_string


missing_field_payloads = [
    {"password": generate_random_string(10), "firstName": generate_random_string(10)},
    {"login": generate_random_string(10), "firstName": generate_random_string(10)},
    {"login": generate_random_string(10), "password": generate_random_string(10)}
]

missing_field_payloads_login = [
    {"password": "1234"},
    {"login": "ninja"}
]

missing_order_parameter_color = [["BLACK"], ["GREY"], ["BLACK", "GREY"], []]
