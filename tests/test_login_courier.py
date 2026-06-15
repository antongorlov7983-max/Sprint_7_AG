import pytest
import allure
import data_test as DT
import helpers as H
from api_client import ScooterApiClient


@allure.feature('Логин курьера')
class TestLoginCourier:

    @allure.story('Успешный логин')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешный логин курьера')
    @allure.description('Проверяем, что курьер может авторизоваться: статус 200 и в ответе есть id')
    def test_login_courier_success(self, create_and_delete_courier):
        api = ScooterApiClient()
        response = api.login_courier(create_and_delete_courier)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.story('Неверные данные')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Логин с неверным паролем')
    @allure.description('Проверяем, что система возвращает 404 при неверном пароле')
    def test_login_wrong_password(self, create_and_delete_courier):
        api = ScooterApiClient()
        payload = {"login": create_and_delete_courier["login"], "password": "0000000"}
        response = api.login_courier(payload)
        assert response.status_code == 404
        assert "message" in response.json()

    @allure.story('Отсутствие обязательных полей')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Логин без одного из полей')
    @allure.description('Параметризованный тест: отсутствует login или password. Ожидаем статус 400')
    @pytest.mark.parametrize('payload', DT.missing_field_payloads_login)
    def test_login_missing_field(self, payload):
        api = ScooterApiClient()
        response = api.login_courier(payload)
        assert response.status_code == 400
        assert "message" in response.json()

    @allure.story('Несуществующий пользователь')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Логин под несуществующим пользователем')
    @allure.description('Проверяем, что система возвращает 404 для случайных логина и пароля')
    def test_login_nonexistent(self):
        api = ScooterApiClient()
        payload = {"login": H.generate_random_string(10), "password": H.generate_random_string(10)}
        response = api.login_courier(payload)
        assert response.status_code == 404
        assert "message" in response.json()
