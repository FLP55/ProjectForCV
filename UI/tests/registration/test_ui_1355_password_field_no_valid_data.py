import pytest
import allure

from API.test_framework.data.email.real_email import invalid_password
from UI.test_framework.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@pytest.mark.parametrize("expected_password", invalid_password)
@allure.id("1355")
@allure.title("1355 Ввод не валидных данных в поле Пароль")
def test_ui_1355_password_field_no_valid_data(browser, expected_password):
    page = MainPage(browser)
    # Открытие страницы регистрации
    page.open_registration_page()
    # Ввод данных в поле Электронная почта
    page.enter_data_to_password_reg_field(password=expected_password)
    # Проверка наличия сообщения
    page.check_error_about_mismatch_password()