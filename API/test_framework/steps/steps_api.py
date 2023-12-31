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

    @allure.step("Получение данных о пользователе")
    def get_data_about_user(self):
        response = self.request.get_user_info()
        CommonChecker.check_status_code_200(response, assertion_message="Данные не получен")

    @allure.step("Редактирование профиля")
    def edit_profile(self, first_name, second_name, last_name, phone_number) -> Any:
        payload = self.data.get_payload_for_changes_data_about_user(first_name, second_name, last_name, phone_number)
        response = self.request.change_user_info(payload)
        CommonChecker.check_status_code_200(response, assertion_message="Данные не изменены")

    @allure.step("Удаление мл-модели")
    def delete_model(self, id_ml) -> Any:
        response = self.request.delete_ml_models(id_ml=id_ml)
        return response

    @allure.step("Создание модели")
    def create_model(self, id, name, model_type, description) -> Any:
        payload = self.data.get_payload_for_create_model(id, name, model_type, description)
        response = self.request.create_model(payload)
        return response

    @allure.step("Проверка успешности создание модели")
    def check_success_create_model(self) -> Any:
        response = self.create_model()
        CommonChecker.check_status_code_200(response, assertion_message="Модель не создалась")

    @allure.step("Проверка не успешности создание модели")
    def check_un_success_create_model(self) -> Any:
        response = self.create_model()
        CommonChecker.check_status_code_400(response, assertion_message="Модель создалась")

    @allure.step("редактирование модели")
    def edit_model(self, id_ml, name, model_type, description) -> Any:
        payload = self.data.get_payload_for_edit_model(name, model_type, description)
        response = self.request.edit_model(payload, id_ml)
        return response

    @allure.step("Проверка успешности редактирования модели")
    def check_success_edit_model(self) -> Any:
        response = self.edit_model()
        CommonChecker.check_status_code_200(response, assertion_message="Модель не отредактировалась")

    @allure.step("Проверка не успешности редактирования модели")
    def check_un_success_edit_model(self) -> Any:
        response = self.edit_model()
        CommonChecker.check_status_code_400(response, assertion_message="Модель создалась")
