import allure
import pytest

from API.test_framework.data.email.real_email import boundary_password
from API.test_framework.steps.steps_api import ApiSteps


@allure.id("1073")
@allure.title("Граничные значения пароля")
@pytest.mark.parametrize("boundary_data", boundary_password)
def test_api_1073_try_reg_user_with_boundary_data_password(boundary_data):
    ApiSteps().check_status_code_after_register_with_invalid_data(
        email="Pavel123@mail.ru", password=boundary_data, confirm_password=boundary_data
    )