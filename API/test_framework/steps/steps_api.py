from typing import Any

import allure

from API.app_data.requests_project.requests import RequestsForTestSait
from API.test_data.api_data import DataClient
from API.test_framework.api_checkers.checkers import CheckersApi
from API.test_framework.helpers.main_checkers import CommonChecker


class ApiSteps:
    def __init__(self) -> None:
        self.request = RequestsForTestSait()
        self.checker = CheckersApi()
        self.data = DataClient()

    @allure.step("Регистрация пользователя валидная")
    def registration_user(self, email, password, confirm_password) -> Any:
        payload = self.data.get_payload_for_registration_user(email, password, confirm_password)
        response = self.request.reg_client(payload)
        CommonChecker.check_status_code_201(response, assertion_message="Не удалось зарегистрировать клиента клиента")
        return response

    @allure.step("Регистрация пользователя невалидная")
    def registration_user_invalid(self, email, password, confirm_password) -> Any:
        payload = self.data.get_payload_for_registration_user(email, password, confirm_password)
        response = self.request.reg_client(payload)
        CommonChecker.check_status_code_400(response, assertion_message="Удалось зарегистрировать клиента клиента")
        return response

    @allure.step("Удаление токена, logout пользователя")
    def logout_user(self) -> Any:
        request = self.request.logout_user_token()
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось удалить токен авторизации")
        return request
