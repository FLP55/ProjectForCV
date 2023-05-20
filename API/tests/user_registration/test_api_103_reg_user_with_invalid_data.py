import allure
import pytest

from API.test_framework.data.email.real_email import invalid_emails, password
from API.test_framework.steps.steps_api import ApiSteps


@allure.id("103")
@allure.title("103 Регистрация пользователя валидная")
@pytest.mark.parametrize("boundary_data", invalid_emails)
def test_api_103_reg_user_with_invalid_data(boundary_data):
    ApiSteps().check_status_code_after_register_with_invalid_data(
        email="boundary_data", password=password, confirm_password=password
    )