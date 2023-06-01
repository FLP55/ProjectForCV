
import pytest
import allure

from API.test_framework.data.email.real_email import invalid_emails
from UI.test_framework.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@pytest.mark.parametrize("expected_email", invalid_emails)
@allure.id("1354")
@allure.title("Ввод невалидных данный в поле Электронная почта")
def test_ui_1354_email_field_no_valid_data(browser, expected_email):
    page = MainPage(browser)
    # Открытие страницы регистрации
    page.open_registration_page()
    #Ввод данных в поле Электронная почта
    page.enter_data_to_email_reg_field(email=expected_email)
    #Проверка наличия сообщения
    page.check_error_about_mismatch_email()