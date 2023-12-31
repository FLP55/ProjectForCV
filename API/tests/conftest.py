import pytest

from API.test_framework.database.base import DBCreateSession
from API.test_framework.steps.steps_api import ApiSteps
from API.test_framework.data.email.real_email import super_user, email_for_api_user, password, valid_emails

@pytest.fixture(scope="function")
def auth_user():
    ApiSteps().auth_user_get_token(email=email_for_api_user, password=password)
    return auth_user

@pytest.fixture(scope="function")
def delete_data():
    yield delete_data
    #Авторизация суперюезра
    ApiSteps().auth_user_get_token(email=super_user, password=password)
    #Удаление данных
    ApiSteps().delete_users_api(emails=valid_emails)


@pytest.fixture(scope="function")
def auth_user_and_delete_model():
    ApiSteps().auth_user_get_token(email=email_for_api_user, password=password)
    return auth_user_and_delete_model
    yield auth_user_and_delete_model
    ApiSteps().delete_model(id_ml="1023")