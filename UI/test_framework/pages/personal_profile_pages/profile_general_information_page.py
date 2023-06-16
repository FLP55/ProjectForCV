import time

import allure
from selenium.webdriver import Keys

from API.test_framework.helpers.main_checkers import CommonChecker
from UI.app_data.base_page import BasePage
from UI.test_data.url_data import PROFILE_PAGE_URL
from UI.test_framework.data.data_main_page import DataMainPage
from UI.test_framework.data.data_messages import DataMessages
from UI.test_framework.locators.profile_main_page_loc import LocatorsProfileMainPage


class PersonalAreaPage(BasePage):
    def __init__(self, browser, url=None) -> None:
        super().__init__(browser, url)
        self.locators_by = LocatorsProfileMainPage()
        self.data = DataMainPage()
        self.error = DataMessages()
        self.url = PROFILE_PAGE_URL

    @allure.step("Проверка наличия элемента 'Профиль'")
    def check_enaybled_elements_profile(self):
        self.is_element_present(self.locators_by.element_profile)

    @allure.step("Логаут пользователя")
    def logout_user(self):
        self.browser.find_element(*self.locators_by.button_user_menu).click()
        self.browser.find_element(*self.locators_by.button_quit).click()
        self.browser.find_element(*self.locators_by.confirm_quit).click()

    @allure.step("Нажатие на кнопку редактировать")
    def click_edit_button(self):
        self.browser.find_element(*self.locators_by.button_edit_profile).click()

    @allure.step("Редактирование поля Имя")
    def edit_name_field(self, name: str):
        field_name = self.browser.find_element(*self.locators_by.field_name)
        field_name.click()
        field_name.send_keys(Keys.CONTROL + "a")
        field_name.send_keys(Keys.DELETE)
        field_name.send_keys(name)
        return field_name

    @allure.step("Редактирование поля фамилия")
    def edit_second_name_field(self, second_name: str):
        field_second_name = self.browser.find_element(*self.locators_by.field_second_name)
        field_second_name.click()
        field_second_name.send_keys(Keys.CONTROL + "a")
        field_second_name.send_keys(Keys.DELETE)
        field_second_name.send_keys(second_name)
        return field_second_name

    @allure.step("Редактирование поля отчество")
    def edit_last_name_field(self, last_name: str):
        field_last_name = self.browser.find_element(*self.locators_by.field_last_name)
        field_last_name.click()
        field_last_name.send_keys(Keys.CONTROL + "a")
        field_last_name.send_keys(Keys.DELETE)
        field_last_name.send_keys(last_name)
        return field_last_name

    @allure.step("Редактирование поля номер телефона")
    def edit_phone_number_field(self, phone_number: str):
        field_phone_number = self.browser.find_element(*self.locators_by.field_phone_number)
        field_phone_number.click()
        field_phone_number_send = self.browser.find_element(*self.locators_by.field_phone_number_send)
        field_phone_number_send.send_keys(Keys.CONTROL + "a")
        field_phone_number_send.send_keys(Keys.DELETE)
        field_phone_number_send.send_keys(phone_number)
        return field_phone_number

    @allure.step("Нажатие на кнопку сохранить")
    def click_button_confirm(self):
        self.browser.find_element(*self.locators_by.button_confirm_change).click()

    @allure.step("Проверка, что кнопка сохранить изменения кликабельна")
    def check_clickable_button_confirm(self):
        self.wait_element_clickable(*self.locators_by.button_confirm_change)

    @allure.step("Проверка, что сохранение успешно")
    def check_confirm_changes(self):
        self.is_element_present(self.locators_by.message_confirm_change)


    @allure.step("Наличие ошибки о неккоректности символов")
    def check_error_invalid_data(self, locator):
        self.browser.find_element(*self.locators_by.field_phone_number).click()
        error = self.browser.find_element(*locator).text
        CommonChecker.check_field_equals(
            error, self.error.message_invalid_data,
            assertion_message="Символы корректные"
        )
    @allure.step("Наличие ошибки о некорректности номера")
    def check_error_invalid_phone_number(self):
        self.browser.find_element(*self.locators_by.field_second_name).click()
        error = self.browser.find_element(*self.locators_by.error_invalid_data_field_phone_number).text
        CommonChecker.check_field_equals(
            error, self.error.message_invalid_phone_number,
            assertion_message="Символы корректные"
        )
    @allure.step("Клик на кнопку отмена")
    def click_cancel_button(self):
        self.browser.find_element(*self.locators_by.button_cancel_change).click()

    @allure.step("Клик по вкладке 'ML-модели'")
    def click_ml_model(self):
        self.browser.find_element(*self.locators_by.button_ml_model).click()