import allure

from API.test_framework.data.email.real_email import email_for_api_user
from API.test_framework.steps.steps_api import ApiSteps


@allure.id("1421")
@allure.title("Попытка авторизация с неверным паролем")
def test_api_1421_try_auth_user_with_invalid_password():
    ApiSteps().authorization_user_with_invalid_password(email=email_for_api_user, password="qwerty")
