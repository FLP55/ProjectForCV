import allure

from API.test_framework.data.email.real_email import email_for_api_user
from API.test_framework.steps.steps_api import ApiSteps


@allure.id("1423")
@allure.title("Отправка запроса на смену пароля")
def test_api_1423_send_request_for_change_password():
    ApiSteps().check_status_for_change_password(email=email_for_api_user)