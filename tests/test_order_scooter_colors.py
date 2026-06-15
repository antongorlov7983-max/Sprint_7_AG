import pytest
import allure
import data_test as DT
from api_client import ScooterApiClient


@allure.feature('Создание заказа')
class TestOrderScooterColors:

    @allure.story('Цвет самоката')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Создание заказа с разными цветами')
    @allure.description('Параметризованный тест: BLACK, GREY, оба цвета, без цвета. Проверяем наличие track в ответе')
    @pytest.mark.parametrize('color', DT.missing_order_parameter_color)
    def test_create_order_colors(self, color):
        api = ScooterApiClient()
        response = api.create_order(color)
        assert "track" in response.json()
        api.cancel_order(response.json()["track"])
