import allure

from API.test_framework.data.email.real_email import email_for_api_user, password
from UI.test_framework.pages.main_pages.main_page import MainPage


@allure.id("763")
@allure.title("Попытка авторизации с пустыми полями UI")
def test_ui_763_try_auth_with_empty_fields(browser):
    #Попытка авторизации с пустым полем электронной почты
    MainPage(browser).auth_user_without_email(password=password)
    #Очистка полей
    MainPage(browser).clear_all_auth_field()
    #Попытка авторизации с пустым полем пароля
    MainPage(browser).auth_user_without_password(email=email_for_api_user)