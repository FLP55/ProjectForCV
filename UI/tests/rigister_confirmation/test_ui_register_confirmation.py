import time

import allure
import pytest

from UI.test_data.url_data import MAIN_PAGE_URL
from UI.test_framework.data.user_data import email_no_admin, password, name_user, last_name_user, \
    middle_name_user, phone_user, company_name,position_smoke
from UI.test_framework.pages.main_pages.main_page import MainPage
from UI.test_framework.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui_smoke
@allure.id("265")
@allure.title("265 Заполнение профиля пользователя JointML не админ")
def test_ui_c6025107_view_existing_cards(browser):
    # Открытие главной страницы банка
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Авторизация не бизнес админ
    main_page.authorization(email=email_no_admin, password=password)

    # Проверка что профиль не заполнен и мы находимся на нужной нам странице
    profile_main_page = ProfileMainPage(browser, url=browser.current_url)
    profile_main_page.page_title_check()

    # Нажимаем на поле 'Имя'
    profile_main_page.click_field_name()

    # Заполняем поле Имя валидным значением
    profile_main_page.input_field_name(name=name_user)

    # Нажимаем на поле "Фамилия"
    profile_main_page.click_field_last_name()

    # Заполняем поле Фамилия валидными значениями
    profile_main_page.input_field_last_name(last_name=last_name_user)

    # Нажимаем на поле Отчество
    profile_main_page.click_middle_name_field()

    # Заполняем поле Отчество валидными значениями
    profile_main_page.input_field_middle_name(middle_name=middle_name_user)

    # Нажимаем на поле Номер телефона
    profile_main_page.click_phone_field()

    # Заполняем поле Номер телефона
    profile_main_page.input_phone_field(phone=phone_user)

    # Нажимаем на поле Ваша организация
    profile_main_page.click_company_field()

    # Заполняем поле Ваша организация
    profile_main_page.input_company_field(company=company_name)

    # Нажимаем на поле Должность
    profile_main_page.click_position_field()

    # Заполняем поле Должность
    profile_main_page.input_position_field(position=position_smoke)
    time.sleep(1)
    # Нажимаем на кнопку продолжить
    # profile_main_page.click_button_continue()
