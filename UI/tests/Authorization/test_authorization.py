import time

import allure
import pytest

from UI.test_data.url_data import MAIN_PAGE_URL
from UI.test_framework.data.for_tests.data_C6109142 import email_smoke_test, valid_password
from UI.test_framework.pages.main_pages.main_page import MainPage


@pytest.mark.ui_smoke
@allure.id("128")
@allure.title("128. Авторизация пользователя по Email с валидными данными")
def test_ui_128_authorization_by_phone_valid(browser):
    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    time.sleep(1)
    # Нажать на поле "Электронная почта"
    main_page.click_on_the_email_field()
    time.sleep(0.2)
    # Ввести валидный email в поле "Электронная почта"
    main_page.enter_on_the_email_field(email=email_smoke_test)
    time.sleep(0.2)
    # Нажать на поле ввода "Пароль"
    main_page.click_on_the_password_input_field()
    time.sleep(0.2)
    # Ввести валидный пароль
    main_page.enter_password_in_pass_field_login(password=valid_password)
    time.sleep(1)
    # Нажать на кнопку "Войти"
    main_page.click_on_button_login()
