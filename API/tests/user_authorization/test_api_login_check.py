import allure

from API.test_framework.steps.steps_api import ApiSteps
from API.test_framework.data.email.real_email import super_user
from API.test_framework.data.password_for_registration.password import passw_valid

@allure.id("108")
@allure.title("108. Проверка авторизации")
def test_api_108_login_check() -> None:
    # Авторизация супер юзера и получение токена
    ApiSteps().auth_user_get_token(email=super_user, password=passw_valid)

    check = ApiSteps().login_check()
    print(check.text)
