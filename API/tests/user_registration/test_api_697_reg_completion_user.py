import allure

from API.test_framework.data.client.client_status import status_user
from API.test_framework.data.client.name_users import name_user
from API.test_framework.data.email.real_email import smoke_user_mail
from API.test_framework.steps.steps_api import ApiSteps
from API.test_framework.data.password_for_registration.password import passw_valid


@allure.id("697")
@allure.title("697. Заполнение валидными данными пользователя не Бизнес Админ")
def test_api_117_register_completion_user() -> None:
    # Авторизация пользователя и получение токена
    ApiSteps().auth_user_get_token(email=smoke_user_mail, password=passw_valid)

    # Заполнение валидными данными не админ
    ApiSteps().register_completion(name=name_user, status=status_user)



