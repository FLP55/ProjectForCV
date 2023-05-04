import allure

from API.test_framework.helpers.main_checkers import CommonChecker
from UI.test_data.url_data import MAIN_PAGE_URL
from UI.test_framework.data.data_messages import DataMessages
from UI.test_framework.data.data_tabs import DataTabs
from UI.test_framework.locators.profile_main_page_loc import LocatorsProfileMainPage
from UI.test_framework.pages.base_pages.base_page import BasePage


class ProfileMainPage(BasePage):
    def __init__(self, browser, url=None) -> None:
        super().__init__(browser, url)
        self.locators_by = LocatorsProfileMainPage
        self.url = MAIN_PAGE_URL
    tab = DataTabs()

    @allure.step("Проверка заголовка страницы не заполненного пользователя")
    def page_title_check_not_confirm(self):
        profile_general_information_page = self.browser.find_element(*self.locators_by.logo_JointML).text
        CommonChecker.check_field_equals(profile_general_information_page, self.tab.not_confirm_page_title,
                                         assertion_message="Ошибка отображения вкладки 'Общая информация'")

    @allure.step("Проверка заголовка страницы заполненного пользователя")
    def page_title_check_confirm(self):
        profile_general_information_page = self.browser.find_element(*self.locators_by.header_confirm_user_locator).text
        CommonChecker.check_field_equals(profile_general_information_page, self.tab.confirm_page_title,
                                         assertion_message="Ошибка отображения вкладки 'Общая информация'")

    @allure.step("Клик на поле Имя")
    def click_field_name(self):
        profile_completion = self.browser.find_element(*self.locators_by.name_field_locator)
        profile_completion.click()

    @allure.step("Заполнить поле Имя")
    def input_field_name(self, name: str):
        profile_completion = self.browser.find_element(*self.locators_by.name_field_locator)
        profile_completion.send_keys(name)

    @allure.step("Клик на поле Фамилия")
    def click_field_last_name(self):
        profile_completion = self.browser.find_element(*self.locators_by.last_name_field_locator)
        profile_completion.click()

    @allure.step("Заполнить поле Фамилия")
    def input_field_last_name(self, last_name: str):
        profile_completion = self.browser.find_element(*self.locators_by.last_name_field_locator)
        profile_completion.send_keys(last_name)

    @allure.step("Клик на поле Отчество")
    def click_middle_name_field(self):
        profile_completion = self.browser.find_element(*self.locators_by.middle_name_field_locator)
        profile_completion.click()

    @allure.step("Заполнить поле Отчество")
    def input_field_middle_name(self, middle_name: str):
        profile_completion = self.browser.find_element(*self.locators_by.middle_name_field_locator)
        profile_completion.send_keys(middle_name)

    @allure.step("Клик на поле 'Номер телефона'")
    def click_phone_field(self):
        profile_completion = self.browser.find_element(*self.locators_by.phone_field_locator)
        profile_completion.click()

    @allure.step("Заполнить поле 'Номер телефона'")
    def input_phone_field(self, phone):
        profile_completion = self.browser.find_element(*self.locators_by.phone_field_locator)
        profile_completion.send_keys(phone)

    @allure.step("Клик на поле 'Ваша организация'")
    def click_company_field(self):
        profile_completion = self.browser.find_element(*self.locators_by.company_field_locator)
        profile_completion.click()

    @allure.step("Заполнить поле 'Ваша организация'")
    def input_company_field(self, company):
        profile_completion = self.browser.find_element(*self.locators_by.company_field_locator)
        profile_completion.send_keys(company)

    @allure.step("Клик на поле 'Должность'")
    def click_position_field(self):
        profile_completion = self.browser.find_element(*self.locators_by.position_field_locator)
        profile_completion.click()

    @allure.step("Заполнить поле 'Должность'")
    def input_position_field(self, position):
        profile_completion = self.browser.find_element(*self.locators_by.position_field_locator)
        profile_completion.send_keys(position)

    @allure.step("Клик на кнопку 'Продолжить'")
    def click_button_continue(self):
        profile_completion = self.browser.find_element(*self.locators_by.button_continue_locator)
        profile_completion.click()

    @allure.step("Переход в Альянсы")
    def click_alliances(self):
        nav_menu = self.browser.find_element(*self.locators_by.nav_menu_alliance_locator)
        nav_menu.click()

    @allure.step("Клик на кнопку Создать альянс")
    def click_create_alliance(self):
        create_alliance = self.browser.find_element(*self.locators_by.create_alliance_locator)
        create_alliance.click()
