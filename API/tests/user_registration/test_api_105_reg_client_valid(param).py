import allure
import pytest

from API.test_framework.data.email.real_email import valid_emails
from API.test_framework.steps.steps_api import ApiSteps
from API.test_framework.data.password_for_registration.password import passw_valid


@allure.id("105")
@allure.title("105. Регистрация пользователя с валидными данными(параметризован емайл)")
@pytest.mark.parametrize("email", valid_emails)
def test_api_c5978275_reg_no_client_bank(email) -> None:
    # Регистрация пользователей с валидными данными набором эмайлов и паролей
    ApiSteps().registration_user(email, password=passw_valid, confirm_password=passw_valid)




