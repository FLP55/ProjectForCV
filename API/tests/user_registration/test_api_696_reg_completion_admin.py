import allure

from API.test_framework.data.client.client_status import status_admin
from API.test_framework.data.client.name_users import name_admin
from API.test_framework.data.email.real_email import smoke_admin_mail
from API.test_framework.steps.steps_api import ApiSteps
from API.test_framework.data.password_for_registration.password import passw_valid


@allure.id("698")
@allure.title("698. Заполнение валидными данными пользователя Бизнес Админ")
def test_api_698_register_completion_admin() -> None:
    # Авторизация пользователя и получение токена
    ApiSteps().auth_user_get_token(email=smoke_admin_mail, password=passw_valid)

    # Заполнение валидными данными не админ
    ApiSteps().register_completion(name=name_admin, status=status_admin)
