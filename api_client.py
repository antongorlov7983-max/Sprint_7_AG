import requests
import allure
from helpers import new_order


class ScooterApiClient:

    base_url = 'https://qa-scooter.praktikum-services.ru'
    endpoint_login = '/api/v1/courier/login'
    endpoint_register = '/api/v1/courier'
    endpoint_delete = '/api/v1/courier/'
    endpoint_order = '/api/v1/orders'
    endpoint_get_list_orders = '/api/v1/orders'
    endpoint_accept_order = '/api/v1/orders/accept/'
    endpoint_get_order = '/api/v1/orders/track'
    endpoint_delet_order = '/api/v1/orders/cancel'

    # === Курьер ===
    @allure.step('Создание курьера')
    def create_courier(self, data_reg):
        payload = {
            "login": data_reg.get("login"),
            "password": data_reg.get("password"),
            "firstName": data_reg.get("firstName")
        }
        return requests.post(f'{self.base_url}{self.endpoint_register}', json=payload)

    @allure.step('Логин курьера')
    def login_courier(self, login_pass):
        payload = {
            "login": login_pass.get("login"),
            "password": login_pass.get("password")
        }
        return requests.post(f'{self.base_url}{self.endpoint_login}', json=payload)

    @allure.step('Удаление курьера')
    def delete_courier(self, courier_id=None):
        url = f'{self.base_url}{self.endpoint_delete}'
        if courier_id:
            url += str(courier_id)
        return requests.delete(url)

    # === Заказы ===
    @allure.step('Создание заказа')
    def create_order(self, color=None):
        return requests.post(f'{self.base_url}{self.endpoint_order}', json=new_order(color))

    @allure.step('Получение списка заказов')
    def get_orders_list(self, params=None):
        return requests.get(f'{self.base_url}{self.endpoint_get_list_orders}', params=params)

    @allure.step('Получение заказа по треку')
    def get_order_by_track(self, order_data):
        return requests.get(f'{self.base_url}{self.endpoint_get_order}', params={'t': order_data["track"]})

    @allure.step('Отмена заказа')
    def cancel_order(self, track):
        return requests.put(f'{self.base_url}{self.endpoint_delet_order}', params={'track': track})

    @allure.step('Принятие заказа')
    def accept_order(self, order_id=None, courier_id=None):
        return requests.put(
            f'{self.base_url}{self.endpoint_accept_order}{order_id}',
            params={'courierId': courier_id}
        )
