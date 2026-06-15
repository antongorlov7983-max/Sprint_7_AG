import allure
import helpers as H
from api_client import ScooterApiClient


@allure.feature('Удаление курьера')
class TestDeleteCourier:

    @allure.story('Успешное удаление')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Успешное удаление курьера')
    @allure.description('Проверяем, что курьер удаляется: статус 200 и тело {"ok": true}')
    def test_delete_courier_success(self):
        api = ScooterApiClient()
        courier_data = H.register_new_courier_and_return_login_password()
        courier_id = api.login_courier(courier_data).json()['id']
        response = api.delete_courier(courier_id)
        assert response.status_code == 200
        assert response.json()["ok"] == True

    @allure.story('Без id')
    @allure.severity(allure.severity_level.MINOR)
    @allure.title('Удаление курьера без id')
    @allure.description('Проверяем, что запрос без id возвращает 404')
    def test_delete_courier_no_id(self):
        api = ScooterApiClient()
        response = api.delete_courier()
        assert response.status_code == 404

    @allure.story('Несуществующий id')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Удаление курьера с несуществующим id')
    @allure.description('Проверяем, что запрос с несуществующим id возвращает 404')
    def test_delete_courier_nonexistent_id(self):
        api = ScooterApiClient()
        response = api.delete_courier("99999")
        assert response.status_code == 404
        assert "message" in response.json()
