import allure
import pytest

from API.test_framework.data.email.real_email import invalid_emails, password
from API.test_framework.steps.steps_api import ApiSteps


@allure.id("1420")
@allure.title("Попытка авторизации с не валидными данными")
@pytest.mark.parametrize("boundary_data", invalid_emails)
def test_api_1420_auth_with_invalid_data(boundary_data):
    ApiSteps().authorization_user_with_invalid_email(email=boundary_data, password=password)