import pytest
import allure
from api_client import ScooterApiClient


@allure.feature('Получение заказа по треку')
class TestGetOrderByTrack:

    @allure.story('Успешное получение')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешное получение заказа по треку')
    @allure.description('Проверяем, что заказ находится по track: статус 200 и в ответе есть объект "order"')
    def test_get_order_by_track_success(self, create_and_delete_order):
        api = ScooterApiClient()
        order_data = {"track": create_and_delete_order['track']}
        response = api.get_order_by_track(order_data)
        assert response.status_code == 200
        assert "order" in response.json()

    @allure.story('Без трека')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Получение заказа без трека')
    @allure.description('Проверяем, что запрос без track возвращает 400')
    def test_get_order_no_track(self):
        api = ScooterApiClient()
        order_data = {"track": None}
        response = api.get_order_by_track(order_data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @allure.story('Несуществующий трек')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Получение заказа по несуществующему треку')
    @allure.description('Проверяем, что запрос с несуществующим track возвращает 404')
    def test_get_order_nonexistent_track(self):
        api = ScooterApiClient()
        order_data = {"track": "999999"}
        response = api.get_order_by_track(order_data)
        assert response.status_code == 404
        assert response.json()["message"] == "Заказ не найден"
