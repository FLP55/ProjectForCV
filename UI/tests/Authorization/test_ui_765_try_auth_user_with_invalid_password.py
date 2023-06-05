

import allure
import pytest

from API.test_framework.data.email.real_email import email_for_api_user
from UI.test_framework.pages.main_pages.main_page import MainPage



@pytest.mark.ui
@allure.id("765")
@allure.title("Попытка авторизации с не валидными данными поле Пароль")
def test_ui_765_try_auth_user_with_invalid_password(browser):
    #Авторизация пользователя
    MainPage(browser).auth_user(email=email_for_api_user, password="123456789")
    # Проверка наличия сообщения
    MainPage(browser).check_error_about_invalid_password()