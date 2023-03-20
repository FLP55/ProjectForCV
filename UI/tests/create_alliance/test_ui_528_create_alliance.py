
import allure
import pytest

from UI.test_data.url_data import MAIN_PAGE_URL
from UI.test_framework.data.for_tests.data_alliances import name_alliance, descriptions
from UI.test_framework.data.user_data import email_no_admin, password
from UI.test_framework.helpers.data_generation import get_custom_alliance_name
from UI.test_framework.pages.main_pages.main_page import MainPage
from UI.test_framework.pages.profile_pages.profile_alliance_page import ProfileAlliancePage
from UI.test_framework.pages.profile_pages.profile_main_page import ProfileMainPage


@pytest.mark.ui_smoke
@allure.id("562")
@allure.title("562 Создание альянса")
def test_ui_528_create_alliance(browser):
    # Получение рандомного Названия Альянса
    random_name = get_custom_alliance_name()

    # Открытие главной страницы
    main_page = MainPage(browser, MAIN_PAGE_URL)
    main_page.open()

    # Авторизация не бизнес админ
    main_page.authorization(email=email_no_admin, password=password)

    # Проверка что профиль заполнен и мы находимся на нужной нам странице
    profile_main_page = ProfileMainPage(browser)
    profile_main_page.page_title_check_confirm()

    # Переход в Алянсы
    profile_main_page.click_alliances()

    # Клик на кнопку Создать Альянс
    profile_main_page.click_create_alliance()

    # Нажимаем на кнопку с информацией
    profile_alliance_page = ProfileAlliancePage(browser)
    profile_alliance_page.click_info_button()

    # Клик на кнопку открытия закрытия Альянса
    profile_alliance_page.click_checkbox_open_close()

    # Клик на поле Название альянса
    profile_alliance_page.click_field_alliance_name()

    # Заполнить поле Название альянса
    profile_alliance_page.input_field_alliance_name(name_alliance=random_name)

    # Клик на отрасль Альянса из выпадающего списка
    profile_alliance_page.click_industry_dropdown()

    # Выбрать отрасль из выпадающего списка
    profile_alliance_page.select_industry()

    # Клик на поле Описание альянса
    profile_alliance_page.click_description()

    # Заполнение поля Описание альянса
    profile_alliance_page.input_field_description(descriptions=descriptions)

    # Клик на кнопку Сохранить
    profile_alliance_page.click_button_save()

    # Клик на вкладку Созданные
    profile_alliance_page.click_on_the_created_tab()

    # Проверка что Альянс отображается во вкладке созданные
    profile_alliance_page.checking_alliance_the_display_in_the_system()
