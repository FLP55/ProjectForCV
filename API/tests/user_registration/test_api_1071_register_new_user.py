import allure

from API.test_framework.data.email.real_email import email_for_reg, password
from API.test_framework.steps.steps_api import ApiSteps


@allure.id("1071")
@allure.title("1071.Регистрация пользователя")
def test_api_1071_register_new_user(delete_data):
    ApiSteps().check_status_code_after_register_with_valid_data(
        email=email_for_reg, password=password, confirm_password=password
    )