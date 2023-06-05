import allure
import pytest

from API.test_framework.data.email.real_email import email_for_api_user
from UI.test_framework.pages.main_pages.main_page import MainPage



@pytest.mark.ui
@allure.id("1486")
@allure.title("Смена пароля автотест")
def test_ui_1486_change_password(browser):
    MainPage(browser).change_password(email=email_for_api_user)
