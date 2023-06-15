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

    @allure.step("клик по модели")
    def click_to_model(self):
        self.browser.find_element(*self.locators_by.button_model).click()

    @allure.step('клик по кнопке редактировать модель')
    def click_edit_model(self):
        self.is_element_present(self.locators_by.button_edit_model)
        self.browser.find_element(*self.locators_by.button_edit_model).click()

    @allure.step("Редактирование поля имя мл-модели")
    def input_field_name(self, name):
        field = self.browser.find_element(*self.locators_by.field_name)
        field.click()
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(name)
        return field

    @allure.step("Редактирование поля тип мл-модели")
    def input_field_type(self, type):
        field = self.browser.find_element(*self.locators_by.type_field)
        field.click()
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(type)
        return field

    @allure.step("Клик на кнопку сохранить")
    def click_save_button(self):
        self.browser.find_element(*self.locators_by.button_save_change).click()

    @allure.step("Попытка перехода на другую вкладку, без сохранения")
    def try_switch_tab(self):
        self.browser.find_element(*self.locators_by.tab_ml_models).click()
        self.browser.find_element(*self.locators_by.button_submit_switch).click()
        self.is_element_present(self.locators_by.header)

