import allure

from API.test_framework.data.email.real_email import email_gmail_private
from API.test_framework.steps.steps_api import ApiSteps
from API.test_framework.data.password_for_registration.password import passw_valid


@allure.id("C6109145")
@allure.title("C6109145. Регистрация пользователя в приложении")
def test_api_C6109145_auth_valid() -> None:
    # Регистрация пользователей с валидными данными набором эмайлов и паролей
    ApiSteps().authorization_user(email=email_gmail_private, password=passw_valid)

