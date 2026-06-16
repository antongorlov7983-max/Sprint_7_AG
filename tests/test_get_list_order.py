import allure
from api_client import ScooterApiClient


@allure.feature('Список заказов')
class TestGetListOrders:

    @allure.story('Получение списка')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Получение списка заказов')
    @allure.description('Проверяем, что в ответе есть ключ "orders" и его значение — список')
    def test_get_orders_list(self):
        api = ScooterApiClient()
        response = api.get_orders_list()
        assert "orders" in response.json()
        assert type(response.json()["orders"]) == list
