import allure

from API.test_framework.data.email.real_email import smoke_user_mail
from API.test_framework.database.queries.userservicedb import QueriesUserService
from API.test_framework.steps.steps_api import ApiSteps
from API.test_framework.data.password_for_registration.password import passw_valid


@allure.id("232")
@allure.title("232. Регистрация тестового юзера (e2e)")
def test_api_232_reg_test_user_e2e() -> None:
    # Регистрация пользователя с валидными данными набором эмайлов и паролей
    ApiSteps().registration_user(email=smoke_user_mail, password=passw_valid, confirm_password=passw_valid)

    # Подтверждение юзера через БД
    QueriesUserService().confirm_email_user(user=smoke_user_mail)

