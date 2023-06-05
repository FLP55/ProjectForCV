from typing import Any

import allure

from API.app_data.requests_project.requests import RequestsForTestAPI
from API.test_data.api_data import DataClient
from API.test_framework.api_checkers.checkers import CheckersApi
from API.test_framework.helpers.main_checkers import CommonChecker


class ApiSteps:
    def __init__(self) -> None:
        self.request = RequestsForTestAPI()
        self.checker = CheckersApi()
        self.data = DataClient()

    @allure.step("Регистрация пользователя")
    def registration_user(self, email, password, confirm_password) -> Any:
        payload = self.data.get_payload_for_registration_user(email, password, confirm_password)
        response = self.request.reg_client(payload)
        return response
    @allure.step("Проверка статуса регистрации с валидными данными")
    def check_status_code_after_register_with_valid_data(self, email, password, confirm_password) -> Any:
        response = self.registration_user(email, password, confirm_password)
        CommonChecker.check_status_code_201(response, assertion_message="Не удалось зарегистрировать клиента клиента")

    @allure.step("Проверка статуса регистрации с невалидными данными")
    def check_status_code_after_register_with_invalid_data(self, email, password, confirm_password) -> Any:
        response = self.registration_user(email, password, confirm_password)
        CommonChecker.check_status_code_400(response, assertion_message="Удалось зарегистрировать клиента клиента")

    @allure.step("Авторизация пользователя")
    def auth_user(self, email, password) -> Any:
        payload = self.data.get_payload_for_authorization_user(email, password)
        response = self.request.auth_user(payload)
        return response

    @allure.step("Проверка авторизации на успешность")
    # Пользователь подтвержден после регистрации вручную
    def authorization_user(self, email, password) -> Any:
        response = self.auth_user(email, password)
        CommonChecker.check_status_code_202(response, assertion_message="Не удалось авторизоваться")
        return response

    @allure.step("Проверка авторизации на не успешность")
    # Пользователь подтвержден после регистрации вручную
    def authorization_user_with_invalid_email(self, email, password) -> Any:
        response = self.auth_user(email, password)
        CommonChecker.check_status_code_400(response, assertion_message="удалось авторизоваться")
        return response

    @allure.step("Проверка авторизации на не успешность c неверным паролем")
    # Пользователь подтвержден после регистрации вручную
    def authorization_user_with_invalid_password(self, email, password) -> Any:
        response = self.auth_user(email, password)
        CommonChecker.check_status_code_403(response, assertion_message="удалось авторизоваться")
        return response

    @allure.step("Получение токена авторизации")
    def auth_user_get_token(self, email, password):
        auth_user = self.auth_user(email, password)
        csrf_token = auth_user.cookies.get("csrftoken")
        session_id = auth_user.cookies.get("sessionid")
        self.request.cookies['Cookie'] = 'csrftoken=' + csrf_token + ";" + ' sessionid=' + session_id
        return auth_user.cookies

    @allure.step("Удаление пользователей")
    # Техникческий метод на удаление всех юзеров после регистраций и созданий альянсов
    def delete_users_api(self, emails) -> Any:
        payload = self.data.get_payload_for_delete_data(emails)
        response = self.request.delete_users(payload)
        CommonChecker.check_status_code_200(response, assertion_message="Не удалось удалить")


    @allure.step("Logout пользователя")
    # Пользователь выходит из системы
    def logout_user(self) -> Any:
        request = self.request.logout_user()
        CommonChecker.check_status_code_202(request, assertion_message="Не удалось выйти")
        return request

    @allure.step("Запрос на изменение пароля")
    def request_for_change_password(self, email) -> Any:
        payload = self.data.get_payload_only_email(email)
        response = self.request.change_password(payload)
        return response

    @allure.step("Проверка на успешность запроса на изменение пароля")
    def check_status_for_change_password(self, email) -> Any:
        response = self.request_for_change_password(email)
        CommonChecker.check_status_code_200(response, assertion_message="Не удалось отправить запрос")

    @allure.step("Проверка на не успешность запроса на изменение пароля")
    def check_status_for_change_password_with_invalid_data(self, email) -> Any:
        response = self.request_for_change_password(email)
        print(response)
        CommonChecker.check_status_code_400(response, assertion_message="Не удалось отправить запрос")

    @allure.step("Подтверждение смены пароля")
    def confirm_change_password(self, token, password, confirm_password) -> Any:
        payload = self.data.get_payload_for_confirm_change_password(token, password, confirm_password)
        response = self.request.confirm_password(payload)
        CommonChecker.check_status_code_200(response, assertion_message="Пароль не изменен")