import pytest
import allure
import data_test as DT
import helpers as H
from api_client import ScooterApiClient


@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.story('Успешное создание')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешное создание курьера')
    @allure.description('Проверяем, что курьера можно создать: статус 201 и тело {"ok": true}')
    def test_create_courier_success(self):
        api = ScooterApiClient()
        payload = {
            "login": H.generate_random_string(10),
            "password": H.generate_random_string(10),
            "firstName": H.generate_random_string(10)
        }
        response = api.create_courier(payload)
        assert response.status_code == 201
        assert response.json()["ok"] == True

        courier_id = api.login_courier(payload).json()['id']
        api.delete_courier(courier_id)

    @allure.story('Дубликат')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Создание дубликата курьера')
    @allure.description('Проверяем, что нельзя создать курьера с уже существующим логином: статус 409')
    def test_create_courier_duplicate(self, create_and_delete_courier):
        api = ScooterApiClient()
        response = api.create_courier(create_and_delete_courier)
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json()["message"]

    @allure.story('Отсутствие обязательных полей')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Создание курьера без одного из полей')
    @allure.description('Параметризованный тест: отсутствует login, password или firstName. Ожидаем статус 400')
    @pytest.mark.parametrize('payload', DT.missing_field_payloads)
    def test_create_courier_missing_field(self, payload):
        api = ScooterApiClient()
        response = api.create_courier(payload)
        assert response.status_code == 400
