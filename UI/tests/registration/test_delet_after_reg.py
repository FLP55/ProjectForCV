import pytest

from API.test_framework.data.email.real_email import super_user, email_ui_reg
from API.test_framework.data.password_for_registration.password import passw_valid
from API.test_framework.steps.steps_api import ApiSteps


@pytest.mark.register_ui
# Технический ендпоинт на удаление емайла
def test_delete_ui_user() -> None:
    # Авторизация супер юзера и получение токена
    ApiSteps().auth_user_get_token(email=super_user, password=passw_valid)
    # Удаление тестовых юзеров
    ApiSteps().delete_users_api(emails=email_ui_reg)
