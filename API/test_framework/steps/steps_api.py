from typing import Any

import allure

from API.app_data.requests_project.requests import RequestsForTestSait, headers
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

    @allure.step("Авторизация пользователя")
    # Пользователь подтвержден после регистрации вручную
    def authorization_user(self, email, password) -> Any:
        payload = self.data.get_payload_for_authorization_user(email, password)
        response = self.request.auth_user(payload)
        CommonChecker.check_status_code_202(response, assertion_message="Не удалось авторизоваться")
        return response

    def auth_user_get_token(self, email, password):
        auth_user = self.authorization_user(email, password)
        csrf_token = auth_user.cookies.get("csrftoken")
        session_id = auth_user.cookies.get("sessionid")
        headers["Cookie"] = f'csrftoken={csrf_token};sessionid={session_id}'

    @allure.step("Удаление пользователей")
    # Техникческий метод на удаление всех юзеров после регистраций и созданий альянсов
    def delete_users_api(self, emails) -> Any:
        payload = self.data.get_payload_for_delete_users(emails=emails)
        response = self.request.delete_users(payload)
        CommonChecker.check_status_code_200(response, assertion_message="Не удалось удалить")

    @allure.step("Удаление пользователя UI")
    # Техникческий метод на удаление всех юзеров после регистраций и созданий альянсов
    def delete_users_ui(self, emails) -> Any:
        payload = self.data.get_payload_for_delete_users(emails=emails)
        response = self.request.delete_users(payload)
        CommonChecker.check_status_code_200(response, assertion_message="Не удалось удалить")

    @allure.step("Logout пользователя")
    # Пользователь выходит из системы
    def logout_user(self) -> Any:
        request = self.request.logout_user()
        CommonChecker.check_status_code_202(request, assertion_message="Не удалось выйти")
        return request

    @allure.step("Заполнение данными пользователя(Не бизнес Админ")
    # Заполнение после регистрации
    def register_complition(self):
        payload = self.data.get_payloda_register_complition()
        request = self.request.register_completion(payload)
        CommonChecker.check_status_code_201(request, assertion_message="Не удалось заполнить")
        return request

    @allure.step("Login check")
    # Пользователь выходит из системы
    def login_check(self) -> Any:
        request = self.request.login_check()
        CommonChecker.check_status_code_200(request, assertion_message="Не удалось проверить")
        return request
