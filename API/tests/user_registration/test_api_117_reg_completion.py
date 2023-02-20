import allure

from API.test_framework.data.email.real_email import smoke_mail, smoke_mail2, super_user
from API.test_framework.steps.steps_api import ApiSteps
from API.test_framework.data.password_for_registration.password import passw_valid


@allure.id("117")
@allure.title("117. Заполнение валидными данными пользователя не Бизнес Админ")
def test_api_117_register_completion() -> None:
    # Регистрация пользователя
    ApiSteps().registration_user(email=smoke_mail, password=passw_valid, confirm_password=passw_valid)

    # Тут надо дописать проверку на подтверждение юзера через БД

    # Авторизация пользователя и получение токена
    ApiSteps().auth_user_get_token(email=smoke_mail, password=passw_valid)

    # Заполнение валидными данными не админ
    ApiSteps().register_complition()

    # Авторизация супер юзера и получение токена
    ApiSteps().auth_user_get_token(email=super_user, password=passw_valid)

    # Удаление тестового юзера
    ApiSteps().delete_users_api(emails=smoke_mail2)
