import allure

from API.test_framework.steps.steps_api import ApiSteps
from API.test_framework.data.email.real_email import super_user, valid_emails
from API.test_framework.data.password_for_registration.password import passw_valid

@allure.id("166")
@allure.title("166. Удаление тестовых юзеров")
def test_api_166_delete_users() -> None:
    # Авторизация супер юзера и получение токена
    ApiSteps().auth_user_get_token(email=super_user, password=passw_valid)
    # Удаление тестовых юзеров
    ApiSteps().delete_users_api(emails=valid_emails)
