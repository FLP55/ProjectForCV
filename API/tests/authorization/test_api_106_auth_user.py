import allure

from API.test_framework.data.email.real_email import email_for_api_user, password
from API.test_framework.steps.steps_api import ApiSteps


@allure.id("106")
@allure.title("Авторизация пользователя с валидными данными")
def test_api_106_auth_user():
    ApiSteps().authorization_user(email=email_for_api_user, password=password)