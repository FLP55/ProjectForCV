import allure
import pytest
from selenium.webdriver.common.keys import Keys

from test_framework.helpers.main_checkers import CommonChecker
from test_framework.ui.data.data_messages import DataMessages
from test_framework.ui.data.data_main_page import DataMainPage
from test_framework.ui.data.for_tests.data_c5993625 import full_password
from test_framework.ui.data.for_tests.data_c5994510 import full_phone_number
from test_framework.ui.locators.main_page_loc import LocatorsMainPage
from test_framework.ui.pages.base_pages.base_page import BasePage


class MainPage(BasePage):
    locators_by = LocatorsMainPage
    data = DataMainPage()
    error = DataMessages()

    @allure.step('Клик на кнопку "Зарегистрироваться".')
    def open_registration_page(self):
        pass

