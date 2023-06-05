import allure
import pytest

from API.test_framework.data.email.real_email import password
from UI.test_framework.locators.main_page_loc import LocatorsMainPage
from UI.test_framework.pages.main_pages.main_page import MainPage



@pytest.mark.ui
@allure.id("764")
@allure.title("Попытка авторизации с не валидными данными поле Электронная почта UI")
def test_ui_746_try_auth_user_with_invalid_email(browser):
    #Авторизация пользователя
    MainPage(browser).auth_user(email="pavelmail.ru", password=password)
    # Проверка наличия сообщения
    MainPage(browser).check_error_about_mismatch_email(LocatorsMainPage().error_about_mismatch_email_auth)
    # Проверка, что кнопка Войти не активна
    MainPage(browser).check_disabled_button_enter()