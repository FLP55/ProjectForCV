import allure

from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.data_field import DataField
from test_framework.ui.data.data_tabs import DataTabs
from test_framework.ui.locators.personal_profile_pages_loc.profile_general_information_page_loc import (
    LocatorsProfileGeneralInformationPage,
)
from test_framework.ui.pages.base_pages.base_page import BasePage


class ProfileGeneralInformationPage(BasePage):
    locators_by = LocatorsProfileGeneralInformationPage
    tab = DataTabs()
    field = DataField()

    @allure.step("Клик на вкладку '' ")
    def open_profile_security_page(self):
        pass

