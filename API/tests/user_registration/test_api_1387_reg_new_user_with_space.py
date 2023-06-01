import allure

from API.test_framework.steps.steps_api import ApiSteps


@allure.id("1387")
@allure.title("Регистрация с пробелами")
def test_api_1387_reg_new_user_with_space():
    ApiSteps().check_status_code_after_register_with_invalid_data(
        email="   ", password="  ", confirm_password="  "
    )