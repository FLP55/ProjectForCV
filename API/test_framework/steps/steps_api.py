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

    def authorization_by_phone_and_password(self, phone_number, password):
        pass

    @allure.step("Удаление токена, logout пользователя")
    def logout_user(self) -> Any:
        request = self.request.logout_user_token()
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось удалить токен авторизации")
        return request

