import allure
import pytest

from API.test_framework.data.email.real_email import password, email_for_api_user
from UI.test_framework.pages.main_pages.main_page import MainPage
from UI.test_framework.pages.personal_profile_pages.profile_general_information_page import PersonalAreaPage


@pytest.mark.ui
@allure.id("132")
@allure.title("Авторизация пользователя с валидными данными")
def test_ui_132_auth_user(browser):
    #Авторизация пользователя
    MainPage(browser).auth_user(email=email_for_api_user, password=password)
    #Проверка, что авторизация успешна, элемент отображается на странице
    PersonalAreaPage(browser).check_enaybled_elements_profile()