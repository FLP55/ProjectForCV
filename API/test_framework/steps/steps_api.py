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
        self.request.cookies['Cookie'] = 'csrftoken=' + csrf_token + ";" + ' sessionid=' + session_id
        return auth_user.cookies

    @allure.step("Удаление пользователей")
    # Техникческий метод на удаление всех юзеров после регистраций и созданий альянсов
    def delete_users_api(self, emails) -> Any:
        payload = self.data.get_payload_for_delete_users(emails)
        response = self.request.delete_users(payload)
        CommonChecker.check_status_code_200(response, assertion_message="Не удалось удалить")


    @allure.step("Logout пользователя")
    # Пользователь выходит из системы
    def logout_user(self) -> Any:
        request = self.request.logout_user()
        CommonChecker.check_status_code_202(request, assertion_message="Не удалось выйти")
        return request

    @allure.step("Заполнение данными пользователя")
    # Заполнение после регистрации
    def register_completion(self, name: str, status: bool):
        payload = self.data.get_payloda_register_complition(name, status)
        request = self.request.register_completion(payload)
        CommonChecker.check_status_code_201(request, assertion_message="Не удалось заполнить")
        return request

    @allure.step("Login check")
    # Пользователь выходит из системы
    def login_check(self) -> Any:
        request = self.request.login_check()
        CommonChecker.check_status_code_200(request, assertion_message="Не удалось проверить")
        return request

    def details_about_ml_model(self, id_model) -> Any:
        request = self.request.get_details_about_ml_model(id_model)
        print(request.json())
        CommonChecker.check_status_code_200(request, assertion_message="Модель не добавлена в альянс")
        return request