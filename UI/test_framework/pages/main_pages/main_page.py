import time

import allure


from selenium.webdriver import Keys

from API.test_framework.helpers.main_checkers import CommonChecker
from UI.test_data.url_data import MAIN_PAGE_URL
from UI.test_framework.data.data_messages import DataMessages
from UI.test_framework.data.data_main_page import DataMainPage
from UI.test_framework.locators.main_page_loc import LocatorsMainPage
from UI.test_framework.pages.base_pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, browser, url=None) -> None:
        super().__init__(browser, url)
        self.locators_by = LocatorsMainPage
        self.data = DataMainPage()
        self.error = DataMessages()
        self.url = MAIN_PAGE_URL


    @allure.step('Клик на кнопку "Зарегистрироваться".')
    def open_registration_page(self):
        registration_page = self.browser.find_element(*self.locators_by.button_registration_locator)
        registration_page.click()

    @allure.step('Поле "Электронная почта" Регистрации.')
    def find_email_reg_field(self):
        email_field = self.browser.find_element(*LocatorsMainPage.email_reg_field_locator)
        email_field.click()
        return email_field
    @allure.step('Ввести валидный Email в поле Электронная почта.Регистрации')
    def enter_data_to_email_reg_field(self, email: str):
        email_text_field = self.find_email_reg_field()
        email_text_field.click()
        email_text_field.send_keys(email)

    @allure.step('Поле "Пароль".Регистрации')
    def find_password_reg_field(self):
        password_field = self.browser.find_element(*self.locators_by.password_reg_field_locator)
        return password_field

    @allure.step('Ввод валидного пароля в поле "Пароль" регистрации.')
    def enter_data_to_password_reg_field(self, password):
        enter_field_password = self.find_password_reg_field()
        enter_field_password.click()
        enter_field_password.send_keys(password)

    @allure.step('Поле "Повторите пароль" Регистрации')
    def find_confirm_password_reg_field(self):
        confirm_password_field = self.browser.find_element(*self.locators_by.confirm_password_reg_field_locator)
        return confirm_password_field

    @allure.step('Ввод валидного пароля в поле "Повторите пароль" регистрации.')
    def enter_data_to_confirm_password_reg_field(self, password):
        self.wait_element_clickable(*self.locators_by.confirm_password_reg_field_locator)
        enter_field_password = self.find_confirm_password_reg_field()
        enter_field_password.click()
        enter_field_password.send_keys(password)

    @allure.step('Очистка полей Регистрации')
    def clear_all_reg_field(self):
        self.find_confirm_password_reg_field().send_keys(Keys.CONTROL + "a")
        self.find_confirm_password_reg_field().send_keys(Keys.DELETE)
        self.find_password_reg_field().send_keys(Keys.CONTROL + "a")
        self.find_password_reg_field().send_keys(Keys.DELETE)
        self.find_email_reg_field().send_keys(Keys.CONTROL + "a")
        self.find_email_reg_field().send_keys(Keys.DELETE)

    @allure.step('Кнопка "Продолжить". Регистрации')
    def find_element_button_continue_reg(self):
        button_continue = self.browser.find_element(*self.locators_by.button_continue_reg)
        return button_continue
    @allure.step('Клик на кнопку продолжить. Регистрации')
    def click_to_continue_button_reg(self):
        button = self.find_element_button_continue_reg()
        button.click()

    @allure.step('Проверка что кнопка "Продолжить" не активна')
    def check_button_continue_not_active(self):
        button = self.find_element_button_continue_reg()
        button.is_enabled()

    @allure.step('Нажатие на чекбокс в окне регистрации')
    def click_to_checkbox_in_reg_window(self):
        self.browser.execute_script(self.locators_by.checkbox_reg_locator)

    @allure.step('Проверка наличие ошибки "Пароли не совпадают"')
    def check_error_about_coincidence_password(self):
        text_about_coincidence_password = self.browser.find_element(
            *self.locators_by.error_about_coincidence_password
        ).text
        CommonChecker.check_field_equals(
            text_about_coincidence_password, self.error.message_no_coincidence_passwords,
            assertion_message="Ошибка отображения уведомления о неверном текущем пароле"
        )
    @allure.step('Проверка окно подтверждения регистрации')
    def check_window_about_reg_new_user(self):
        text_on_window_about_reg_new_user = self.browser.find_element(
            *self.locators_by.message_about_reg_new_user
        ).text
        CommonChecker.check_field_equals(
            text_on_window_about_reg_new_user, self.error.message_reg_new_user,
            assertion_message="Пользователь не зарегистрирован"
        )

    @allure.step('Проверка наличия сообщение о вводе некорректного адреса почты')
    def check_error_about_mismatch_email(self, locator):
        error_about_email = self.browser.find_element(*locator).text
        CommonChecker.check_field_equals(
            error_about_email, self.error.message_mismatch_email,
            assertion_message="Электронная почта корректная"
        )

    @allure.step('Проверка наличия сообщение о вводе некорректного пароля. поле регистрации')
    def check_error_about_mismatch_password(self):
        error_about_password = self.browser.find_element(
            *self.locators_by.error_about_mismatch_password
        ).text
        CommonChecker.check_field_equals(
            error_about_password, self.error.message_mismatch_password,
            assertion_message="Пароль корректный"
        )
    @allure.step("Проверка наличия элемента, что пароль неверный. поле авторизации")
    def check_error_about_invalid_password(self):
        text_error = self.browser.find_element(*self.locators_by.error_about_mismatch_password_auth).text
        while text_error != "Неверный пароль.":
            text_error = self.browser.find_element(
                *self.locators_by.error_about_mismatch_password
            ).text
            time.sleep(1)
        CommonChecker.check_field_equals(
            text_error, self.error.message_invalid_password,
            assertion_message="Пароль корректный"
        )
    @allure.step("Авторизация")
    def auth_user(self, email: str, password: str):
        email_field = self.browser.find_element(*self.locators_by.email_auth_field_locator)
        email_field.click()
        email_field.send_keys(email)
        password_field = self.browser.find_element(*self.locators_by.password_auth_field_locator)
        password_field.click()
        password_field.send_keys(password)
        button = self.browser.find_element(*self.locators_by.button_continue_auth)
        button.click()
        time.sleep(3)
    @allure.step("Попытка авторизации без поля email")
    def auth_user_without_email(self, password: str):
        password_field = self.browser.find_element(*self.locators_by.password_auth_field_locator)
        password_field.click()
        password_field.send_keys(password)
        self.browser.find_element(*self.locators_by.button_continue_auth).is_enabled()
    @allure.step("Попытка авторизации без пароля")
    def auth_user_without_password(self, email: str):
        email_field = self.browser.find_element(*self.locators_by.email_auth_field_locator)
        email_field.click()
        email_field.send_keys(email)
        self.browser.find_element(*self.locators_by.button_continue_auth).is_enabled()

    @allure.step('Очистка полей Авторизации')
    def clear_all_auth_field(self):
        email_field = self.browser.find_element(*self.locators_by.email_auth_field_locator)
        email_field.send_keys(Keys.CONTROL + "a")
        email_field.send_keys(Keys.DELETE)
        password_field = self.browser.find_element(*self.locators_by.password_auth_field_locator)
        password_field.send_keys(Keys.CONTROL + "a")
        password_field.send_keys(Keys.DELETE)

    @allure.step("Проверка наличия элемента 'Войти'")
    def check_enaybled_elements_enter(self):
        self.is_element_present(self.locators_by.element_enter)

    @allure.step("Проверка, что кнопка 'Войти' не активна")
    def check_disabled_button_enter(self):
        self.browser.find_element(*self.locators_by.button_continue_auth).is_enabled()

    @allure.step("Смена пароля")
    def change_password(self, email: str):
        self.browser.find_element(*self.locators_by.button_change_password).click()
        email_field = self.browser.find_element(*self.locators_by.field_email_for_change_password)
        email_field.click()
        email_field.send_keys(email)
        self.browser.find_element(*self.locators_by.button_confirm_change_password).click()
        confirm_change = self.browser.find_element(*self.locators_by.confirm_change_password).text
        CommonChecker.check_field_equals(
            confirm_change, self.error.message_confirm_change_password,
            assertion_message="Пароль корректный"
        )