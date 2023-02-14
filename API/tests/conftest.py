import pytest

from API.test_framework.database.base import DBCreateSession
from API.test_framework.steps.steps_api import ApiSteps
from API.test_framework.data.email.real_email import super_user
from API.test_framework.data.password_for_registration.password import passw_valid


@pytest.fixture
def auth_super_user():
    # Авторизация супер юзера
    authorization = ApiSteps().authorization_user(email=super_user, password=passw_valid)
    return authorization


# def authorization_by_phone():
#     def authorization(phone_number: str, password: str):
#         # Авторизация пользователя
#         authorization_json = ApiSteps().authorization_by_phone_and_password(phone_number, password)
#         return authorization_json
#
#     yield authorization
#     ApiSteps().logout_user()

# Подключение сессии и выход из нее по окончанию теста
@pytest.fixture
def get_db_session():
    session = DBCreateSession().create_session()
    try:
        yield session
    finally:
        DBCreateSession().close_session()
