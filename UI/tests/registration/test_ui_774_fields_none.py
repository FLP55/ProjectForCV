import pytest
import allure

from UI.test_framework.helpers.data_generation import get_custom_email
from UI.test_framework.pages.main_pages.main_page import MainPage
from API.test_framework.data.email.real_email import password


@pytest.mark.ui
@allure.id("774")
@allure.title("774 Регистрация пользователя пустые поля UI")
def test_ui_774_fields_none(browser):
    page = MainPage(browser)
    #Открытие страницы регистрации
    page.open_registration_page()
    #Заполнение поля "Пароль" валидными значениями
    page.enter_data_to_password_reg_field(password=password)
    #Клик на пустое поле
    page.find_email_reg_field()
    #Заполнение поля "Подтверждение Пароля" валидными значениями
    page.enter_data_to_confirm_password_reg_field(password=password)
    #Нажатие на соглашение с правилами
    page.click_to_checkbox_in_reg_window()
    #Проверка кнопки Продолжить
    page.check_button_continue_not_active()
    #Очистка полей
    page.clear_all_reg_field()
    #Заполнение поля "Электронная почта"
    page.enter_data_to_email_reg_field(email=get_custom_email())
    #Заполнение поля "Подтверждение Пароля" валидными значениями
    page.enter_data_to_confirm_password_reg_field(password=password)
    #Проверка кнопки Продолжить и наличие ошибка совподения пароля
    page.check_button_continue_not_active()
    page.check_error_about_coincidence_password()
    #Очистка полей
    page.clear_all_reg_field()
    #Заполнение поля "Электронная почта"
    page.enter_data_to_email_reg_field(email=get_custom_email())
    #Заполнение поля "Пароль" валидными значениями
    page.enter_data_to_password_reg_field(password=password)
    #Проверка кнопки Продолжить
    page.check_button_continue_not_active()