import pytest
import allure
from api_client import ScooterApiClient


@allure.feature('Принятие заказа')
class TestAcceptOrder:

    @allure.story('Успешное принятие')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешное принятие заказа')
    @allure.description('Проверяем, что заказ принимается: статус 200 и тело {"ok": true}')
    def test_accept_order_success(self, create_and_delete_courier, create_and_delete_order):
        api = ScooterApiClient()
        response = api.accept_order(
            order_id=create_and_delete_order['id'],
            courier_id=create_and_delete_courier['id']
        )
        assert response.status_code == 200
        assert response.json()["ok"] == True

    @allure.story('Без id курьера')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Принятие заказа без id курьера')
    @allure.description('Проверяем, что запрос без courierId возвращает 400')
    def test_accept_order_no_courier_id(self, create_and_delete_order):
        api = ScooterApiClient()
        response = api.accept_order(
            order_id=create_and_delete_order['id'],
            courier_id=None
        )
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @allure.story('Неверный id курьера')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Принятие заказа с неверным id курьера')
    @allure.description('Проверяем, что запрос с несуществующим courierId возвращает 404')
    def test_accept_order_bad_courier_id(self, create_and_delete_order):
        api = ScooterApiClient()
        response = api.accept_order(
            order_id=create_and_delete_order['id'],
            courier_id="999999"
        )
        assert response.status_code == 404
        assert response.json()["message"] == "Курьера с таким id не существует"

    @allure.story('Без id заказа')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Принятие заказа без id заказа')
    @allure.description('Проверяем, что запрос без order_id возвращает 400')
    def test_accept_order_no_order_id(self, create_and_delete_courier):
        api = ScooterApiClient()
        response = api.accept_order(
            courier_id=create_and_delete_courier['id'],
            order_id=None
        )
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @allure.story('Неверный id заказа')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Принятие заказа с неверным id заказа')
    @allure.description('Проверяем, что запрос с несуществующим order_id возвращает 404')
    def test_accept_order_bad_order_id(self, create_and_delete_courier):
        api = ScooterApiClient()
        response = api.accept_order(
            courier_id=create_and_delete_courier['id'],
            order_id="99999999"
        )
        assert response.status_code == 404
        assert response.json()["message"] == "Заказа с таким id не существует"
