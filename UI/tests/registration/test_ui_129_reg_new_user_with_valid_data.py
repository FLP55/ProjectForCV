import pytest
import allure

from API.test_framework.data.email.real_email import password, email_for_reg
from UI.test_framework.pages.main_pages.main_page import MainPage


@pytest.mark.ui
@allure.id("129")
@allure.title("129 Регистрация пользователя с валидными данными UI")
def test_ui_129_reg_new_user_with_valid_data(browser_for_delete_user):
    # Открытие страницы регистрации
    MainPage(browser_for_delete_user).open_registration_page()
    # Ввод валидных значений в поля
    MainPage(browser_for_delete_user).enter_data_to_email_reg_field(email=email_for_reg)
    MainPage(browser_for_delete_user).enter_data_to_password_reg_field(password=password)
    MainPage(browser_for_delete_user).find_email_reg_field()
    MainPage(browser_for_delete_user).enter_data_to_confirm_password_reg_field(password=password)
    # Нажатие на соглашение с правилами
    MainPage(browser_for_delete_user).click_to_checkbox_in_reg_window()
    # Нажатие на кнопку продолжить
    MainPage(browser_for_delete_user).click_to_continue_button_reg()
    # Проверка наличие текста на странице
    MainPage(browser_for_delete_user).check_window_about_reg_new_user()
