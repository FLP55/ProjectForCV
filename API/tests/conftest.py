import pytest

from test_framework.api.steps.steps_api import ApiSteps
from test_framework.database.base import DBCreateSession


@pytest.fixture(scope="function")
def authorization_by_phone():
    def authorization(phone_number: str, password: str):
        # Авторизация пользователя
        ApiSteps().authorization_by_phone_and_password(phone_number, password)

    yield authorization
    ApiSteps().logout_user()


@pytest.fixture(scope="function")
def authorization_by_passport():
    def authorization(passport_number: str):
        # Авторизация пользователя
        ApiSteps().authorization_by_passport(passport_number)

    yield authorization
    ApiSteps().logout_user()


@pytest.fixture
def get_db_session():
    session = DBCreateSession().create_session()
    try:
        yield session
    finally:
        DBCreateSession().close_session()
