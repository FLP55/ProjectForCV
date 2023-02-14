import allure

from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.data_field import DataField
from test_framework.ui.data.data_tabs import DataTabs
from test_framework.ui.locators.personal_profile_pages_loc.profile_general_information_page_loc import (
    LocatorsProfileGeneralInformationPage,
)

from UI.app_data.base_page import BasePage
from UI.test_framework.locators.main_page_loc import LocatorsMainPage


class ProfileGeneralInformationPage(BasePage):
    locators_by = LocatorsProfileGeneralInformationPage
    tab = DataTabs()
    field = DataField()

    @allure.step('Нажать на поле "Электронная почта".')
    def click_on_the_email_field(self):
        email_field = self.browser.find_element(*LocatorsMainPage.email_field_locator)
        email_field.click()

    @allure.step('Ввести валидный Email в поле Электронная почта.')
    def enter_on_the_email_field(self, email: str):
        email_text_field = self.browser.find_element(*LocatorsMainPage.email_text_field_locator)
        email_text_field.send_keys(email)

    @allure.step("Проверка отображения вкладки 'Уведомления'")
    def check_displaying_tab_notifications(self):
        tab_notifications_text = self.browser.find_element(*self.locators_by.tab_notifications_locator).text
        CommonChecker.check_field_equals(tab_notifications_text, self.tab.notifications,
                                         assertion_message="Ошибка отображения вкладки 'Уведомления'")

    @allure.step("Проверка отображения поля 'Имя'")
    def check_displaying_field_first_name(self):
        field_first_name_text = self.browser.find_element(*self.locators_by.field_first_name_locator).text
        CommonChecker.check_field_equals(field_first_name_text, self.field.first_name,
                                         assertion_message="Ошибка отображения поля 'Имя'")