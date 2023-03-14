import allure

from API.test_framework.data.email.real_email import smoke_admin_mail
from API.test_framework.database.queries.userservicedb import QueriesUserService
from API.test_framework.steps.steps_api import ApiSteps
from API.test_framework.data.password_for_registration.password import passw_valid


@allure.id("698")
@allure.title("698. Регистрация тестового админа(e2e)")
def test_api_698_reg_test_admin_e2e() -> None:
    # Регистрация пользователя с валидными данными набором эмайлов и паролей
    ApiSteps().registration_user(email=smoke_admin_mail, password=passw_valid, confirm_password=passw_valid)

    # Подтверждение админа через БД
    QueriesUserService().confirm_email_user(user=smoke_admin_mail)
