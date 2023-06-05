import allure
import pytest

from API.test_framework.data.email.real_email import password, email_for_api_user
from UI.test_framework.pages.main_pages.main_page import MainPage
from UI.test_framework.pages.personal_profile_pages.profile_general_information_page import PersonalAreaPage


@pytest.mark.ui
@allure.id("1426")
@allure.title("Логаут пользователя")
def test_ui_1426_logout_user(browser):
    #Авторизация пользователя
    MainPage(browser).auth_user(email=email_for_api_user, password=password)
    #Логаут пользователя
    PersonalAreaPage(browser).logout_user()
    #Проверка наличия элемента "Войти"
    MainPage(browser).check_enaybled_elements_enter()
