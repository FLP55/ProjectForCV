import allure
import pytest

from API.test_framework.data.email.real_email import invalid_emails
from API.test_framework.data.password_for_registration.password import passw_inv
from API.test_framework.steps.steps_api import ApiSteps


@allure.id("104")
@allure.title("104. Регистрация пользователя в приложении с невалидными данными")
@pytest.mark.parametrize("valid_email", invalid_emails)
def test_api_c5978275_reg_no_client_bank(valid_email) -> None:
    # Проверка, что Регистрация пользователя не удается с невалидными данными
    ApiSteps().registration_user_invalid(valid_email, password=passw_inv, confirm_password=passw_inv)
