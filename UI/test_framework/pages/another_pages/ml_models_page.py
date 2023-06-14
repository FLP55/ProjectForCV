import time

import allure
from selenium.webdriver import Keys

from API.test_framework.helpers.main_checkers import CommonChecker
from UI.app_data.base_page import BasePage
from UI.test_data.url_data import ML_MODELS
from UI.test_framework.data.data_main_page import DataMainPage
from UI.test_framework.data.data_messages import DataMessages
from UI.test_framework.locators.ml_models_loc import LocatorsMlModels



class MlModels(BasePage):
    def __init__(self, browser, url=None) -> None:
        super().__init__(browser, url)
        self.locators_by = LocatorsMlModels()
        self.data = DataMainPage()
        self.error = DataMessages()
        self.url = ML_MODELS

    @allure.step("клик по кнопке Добавить мл-модель")
    def click_button_create_new_model(self):
        self.browser.find_element(*self.locators_by.button_create_model).click()