import time

import allure
import pytest

from API.test_framework.data.email.real_email import email_ui_reg
from UI.test_data.url_data import MAIN_PAGE_URL
from UI.test_framework.data.for_tests.data_C6109142 import valid_password
from UI.test_framework.pages.main_pages.main_page import MainPage


@pytest.mark.register_ui
@allure.id("232")
@allure.title("232. Регистрация пользователя по Email с валидными данными")
def test_ui_125_registration_valid(browser):
    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Нажать на кнопку "Создать аккаунт"
    main_page.open_registration_page()

    # Нажать на поле "Электронная почта"
    main_page.click_on_the_email_field()

    # Ввести валидный email в поле "Электронная почта"
    main_page.enter_on_the_email_field(email=email_ui_reg)

    # Нажать на поле ввода "Пароль"
    main_page.click_on_the_password_input_field()

    # Ввести валидный пароль
    main_page.enter_password_in_pass_field_register(password=valid_password)

    # Нажать на кнопку отображения пароля
    main_page.click_on_password_display_button()

    # Нажать на поле ввода "Повторите пароль"
    main_page.click_on_the_repeat_password_input_field()

    # Ввести повторно пароль в поле "Повторите пароль"
    main_page.enter_repeat_password_in_pass_field(password=valid_password)

    # Нажать на кнопку отображения пароля в поле "Повторите пароль"
    main_page.click_on_repeat_password_display_button()

    # Нажать на чекбокс "Я даю согласие на обработку персональных данных"
    main_page.click_on_checkbox_personal_data()
    time.sleep(1)
    # script = "return window.getComputedStyle(document.querySelector('body>p.el'),':after').getPropertyValue('content')"
    # print(driver.execute_script(script).strip())
    # Нажать на кнопку "Продолжить"
    main_page.click_on_button_continue()

    # Проверить что страница о завершении регистрации открылась с нужным текстом уведомления
    main_page.check_finish_reg_page_text()

