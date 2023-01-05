import allure
from selenium.webdriver import Keys

from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.data_messages import DataMessages
from test_framework.ui.data.data_profile_page import DataProfilePage
from test_framework.ui.locators.personal_profile_pages_loc.profile_security_page_loc import LocatorsProfileSecurityPage
from test_framework.ui.pages.base_pages.base_page import BasePage


class ProfileSecurityPage(BasePage):
    locators_by = LocatorsProfileSecurityPage
    error = DataMessages
    data = DataProfilePage

    @allure.step("Клик на кнопку 'Изменить пароль'.")
    def click_on_button_change_password(self):
        pass
