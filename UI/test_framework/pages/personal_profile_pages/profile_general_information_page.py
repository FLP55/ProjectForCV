import allure

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

