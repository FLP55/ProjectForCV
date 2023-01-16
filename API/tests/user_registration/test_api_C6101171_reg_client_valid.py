import allure

from API.test_framework.steps.steps_api import ApiSteps


@allure.id("C6101171")
@allure.title("C6101171. Регистрация пользователя в приложении")
def test_api_c5978275_reg_no_client_bank() -> None:
    # Регистрация не клиента банка
    ApiSteps().registration_user()
