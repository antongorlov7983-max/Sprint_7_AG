import pytest
import helpers as H
from api_client import ScooterApiClient


@pytest.fixture
def create_and_delete_courier():
    # Создаём экземпляр API-клиента
    api = ScooterApiClient()
    # Генерируем случайные данные и регистрируем курьера
    courier_data = H.register_new_courier_and_return_login_password()
    # Логинимся под созданным курьером и получаем его id
    courier_data['id'] = api.login_courier(courier_data).json()['id']
    # Отдаём данные тесту
    yield courier_data
    # После теста удаляем курьера по id
    api.delete_courier(courier_data['id'])

@pytest.fixture
def create_and_delete_order():
    # Создаём экземпляр API-клиента
    api = ScooterApiClient()
    order_data = {}
    # Создаём заказ (цвет по умолчанию [])
    response = api.create_order()
    # Сохраняем track из ответа
    order_data['track'] = response.json()['track']
    # По track получаем id заказа
    order_data['id'] = api.get_order_by_track(order_data).json()['order']['id']
    # Отдаём данные тесту
    yield order_data
    # После теста отменяем заказ по track
    api.cancel_order(order_data['track'])
