import time

import allure
import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from API.test_framework.helpers.main_checkers import CommonChecker
from UI.app_data.base_page import BasePage
from UI.test_data.url_data import CREATE_MODEL
from UI.test_framework.data.data_main_page import DataMainPage
from UI.test_framework.data.data_messages import DataMessages
from UI.test_framework.locators.create_new_model_loc import LocatorsCreateModel




class CreateMlModel(BasePage):
    def __init__(self, browser, url=None) -> None:
        super().__init__(browser, url)
        self.locators_by = LocatorsCreateModel()
        self.data = DataMainPage()
        self.error = DataMessages()
        self.url = CREATE_MODEL

    @allure.step("Заполнение поля имя мл-модели")
    def input_field_name(self, name):
        field = self.browser.find_element(*self.locators_by.name_field)
        field.click()
        field.send_keys(name)
        return field

    @allure.step("Заполнение поля тип задач")
    def input_field_type(self):
        self.browser.find_element(*self.locators_by.type_field).click()
        self.browser.find_element(*self.locators_by.type_class).click()


    @allure.step("Заполнение поля категория")
    def input_category_field(self):
        self.browser.find_element(*self.locators_by.category_field).click()
        self.browser.find_element(*self.locators_by.first_category).click()

    @allure.step("Заполнение поля тип мл-модели")
    def input_field_type_ml_model(self, type):
        field = self.browser.find_element(*self.locators_by.type_model_field)
        field.click()
        field.send_keys(type)
        return field

    @allure.step("Заполнение поля Описание")
    def input_field_description(self, description):
        field = self.browser.find_element(*self.locators_by.description_field)
        field.click()
        field.send_keys(description)
        return field

    @allure.step("Клик по тегу Банки")
    def click_tag(self):
        self.browser.find_element(*self.locators_by.teg_bank).click()

    @allure.step("Добавление файла")
    def add_file(self):
        # element = WebDriverWait(self.browser, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='con-input-upload']")))
        # element.click()
        # # Ждем пока откроется окно с выбором файла.
        # time.sleep(10)
        # # Заполняем поле ввода пути и жмем на Enter.
        # keyboard.write(r'E:\Видео для работы\файлы для работы\weights.py')
        # keyboard.press('enter')
        field = self.browser.find_element(*self.locators_by.input_file)
        upload ='E:\Видео для работы\файлы для работы\weights.py'
        field.send_keys(upload)


    @allure.step("клик на кнопку добавить")
    def click_button_add(self):
        self.browser.find_element(*self.locators_by.button_add).click()

    @allure.step('Проверка наличия ошибке о повторном названии модели')
    def check_error_about_repeated_name(self):
        self.wait_elements_located(*self.locators_by.message_about_repeated_name)
        message = self.browser.find_element(*self.locators_by.message_about_repeated_name).text
        CommonChecker.check_field_equals(
            message, self.error.message_repeated_name,
            assertion_message="модель еще не создана"
        )

    @allure.step('Проверка, что кнопка продолжить кликабельна')
    def check_button_continue_active(self):
        button = self.browser.find_element(*self.locators_by.button_add)
        button.is_enabled()

    @allure.step("скрипт запуска файла")
    def disable_opacity(self):
        """ disable all opacity in input[type='file'] """
        return self.browser.execute_script(
            "for (const [key, value] of Object.entries(document.getElementsByTagName('input'))) { value.setAttribute('style', 'opacity: 1') }")