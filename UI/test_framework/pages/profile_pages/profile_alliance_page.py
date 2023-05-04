import time

import allure

from API.test_framework.helpers.main_checkers import CommonChecker
from UI.test_data.url_data import ALLIANCE_PAGE_URL
from UI.test_framework.data.data_messages import DataMessages
from UI.test_framework.data.data_tabs import DataTabs
from UI.test_framework.locators.alliances_page_loc import LocatorsAlliancesPage
from UI.test_framework.pages.base_pages.base_page import BasePage


class ProfileAlliancePage(BasePage):
    def __init__(self, browser, url=None) -> None:
        super().__init__(browser, url)
        self.locators_by = LocatorsAlliancesPage
        self.url = ALLIANCE_PAGE_URL

    tab = DataTabs()
    error = DataMessages()

    @allure.step("Проверка заголовка страницы заполненного пользователя")
    def page_title_check_confirm(self):
        alliance_information_page = self.browser.find_element(*self.locators_by.header_create_alliance_locator).text
        CommonChecker.check_field_equals(alliance_information_page, self.tab.create_alliance_page_tittle,
                                         assertion_message="Ошибка отображения вкладки 'Создание альянса'")

    @allure.step("Кликаем на подсказку")
    def click_info_button(self):
        alliance_create = self.browser.find_element(*self.locators_by.click_info_button_locator)
        alliance_create.click()

    @allure.step("Проверяем текст подсказки в кнопке с информацией")
    def check_info_button(self):
        alliance_created = self.browser.find_element(*self.locators_by.check_info_button_locator).text
        CommonChecker.check_field_equals(alliance_created, self.tab.info_button_text,
                                         assertion_message="Ошибка отображения информации на кнопке")

    @allure.step("Проверяем чекбокс Открытй-Закрытый альянс")
    def click_checkbox_open_close(self):
        alliance_created = self.browser.find_element(*self.locators_by.click_checkbox_open_close)
        alliance_created.click()
        alliance_created.click()

    @allure.step("Клик на поле Название Альянса")
    def click_field_alliance_name(self):
        alliance_create = self.browser.find_element(*self.locators_by.click_name_locator)
        alliance_create.click()

    @allure.step("Заполнение поля Название Альянса")
    def input_field_alliance_name(self, name_alliance: str):
        alliance_create = self.browser.find_element(*self.locators_by.input_name_locator)
        alliance_create.send_keys(name_alliance)

    @allure.step("Кликаем на dropdown отрасль альянса")
    def click_industry_dropdown(self):
        alliance_create = self.browser.find_element(*self.locators_by.industry_dropdown_locator)
        alliance_create.click()

    @allure.step("Выбираем отрасль из выпадающего списка")
    def select_industry(self):
        alliance_create = self.browser.find_element(*self.locators_by.select_industry_locator)
        alliance_create.click()

    @allure.step("Кликаем на поле Описание альянса")
    def click_description(self):
        alliance_create = self.browser.find_element(*self.locators_by.input_description_locator)
        alliance_create.click()

    @allure.step("Заполняем поле Описание альянса")
    def input_field_description(self, descriptions: str):
        alliance_create = self.browser.find_element(*self.locators_by.input_description_locator)
        alliance_create.send_keys(descriptions)

    @allure.step("Клик на кнопку Сохранить")
    def click_button_save(self):
        alliance_create = self.browser.find_element(*self.locators_by.click_button_save)
        alliance_create.click()

    @allure.step("Клик на вкладку Созданные")
    def click_on_the_created_tab(self):
        alliance_created = self.browser.find_element(*self.locators_by.click_created_tab_alliance)
        alliance_created.click()

    @allure.step("Проверяем отображение в системе")
    def checking_alliance_the_display_in_the_system(self):
        alliance_created = self.browser.find_element(*self.locators_by.search_alliance_locator)
        alliance_created.is_displayed()

