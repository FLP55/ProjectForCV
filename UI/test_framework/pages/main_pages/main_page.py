import allure

from API.test_framework.helpers.main_checkers import CommonChecker
from UI.test_framework.data.data_messages import DataMessages
from UI.test_framework.data.data_main_page import DataMainPage
from UI.test_framework.locators.main_page_loc import LocatorsMainPage
from UI.test_framework.pages.base_pages.base_page import BasePage


class MainPage(BasePage):
    locators_by = LocatorsMainPage
    data = DataMainPage()
    error = DataMessages()

    @allure.step('Клик на кнопку "Зарегистрироваться".')
    def open_registration_page(self):
        registration_page = self.browser.find_element(*self.locators_by.button_registration_locator)
        registration_page.click()

    @allure.step('Нажать на поле "Электронная почта".')
    def click_on_the_email_field(self):
        email_field = self.browser.find_element(*LocatorsMainPage.email_field_locator)
        email_field.click()

    @allure.step('Ввести валидный Email в поле Электронная почта.')
    def enter_on_the_email_field(self, email: str):
        email_text_field = self.browser.find_element(*LocatorsMainPage.email_text_field_locator)
        email_text_field.send_keys(email)

    @allure.step('Нажать на поле "Пароль".')
    def click_on_the_password_input_field(self):
        enter_field_password = self.browser.find_element(*self.locators_by.field_password_locator)
        enter_field_password.click()

    @allure.step('Ввод валидного пароля в поле "Пароль" регистрации.')
    def enter_password_in_pass_field_register(self, password):
        enter_field_password = self.browser.find_element(*self.locators_by.password_text_field_locator_register)
        enter_field_password.send_keys(password)

    @allure.step('Ввод валидного пароля в поле "Пароль" авторизация.')
    def enter_password_in_pass_field_login(self, password):
        enter_field_password = self.browser.find_element(*self.locators_by.password_text_field_locator_login)
        enter_field_password.send_keys(password)

    @allure.step("Нажать на кнопку отображения пароля.")
    def click_on_password_display_button(self):
        click_display_button = self.browser.find_element(*self.locators_by.button_hidden_password_locator)
        click_display_button.click()

    @allure.step('Нажать на поле "Повторите пароль".')
    def click_on_the_repeat_password_input_field(self):
        click_field_repeat_password = self.browser.find_element(*self.locators_by.repeat_password_field_locator)
        click_field_repeat_password.click()

    @allure.step('Повторный ввод пароля.')
    def enter_repeat_password_in_pass_field(self, password):
        enter_field_repeat_password = self.browser.find_element(*self.locators_by.repeat_password_field_locator)
        enter_field_repeat_password.send_keys(password)

    @allure.step("Нажать на кнопку отображения пароля в поле повторите пароль.")
    def click_on_repeat_password_display_button(self):
        click_display_button = self.browser.find_element(*self.locators_by.button_hidden_repeat_password_locator)
        click_display_button.click()

    @allure.step("Нажать на чекбокс я даю согласие на обработку персональных данных")
    def click_on_checkbox_personal_data(self):
        click_checkbox_data = self.browser.find_element(*self.locators_by.checkbox_personal_data)
        click_checkbox_data.click()

    @allure.step("Нажать на кнопку продолжить")
    def click_on_button_continue(self):
        click_button_continue = self.browser.find_element(*self.locators_by.button_continue)
        click_button_continue.click()

    @allure.step('Проверяем что на почту отправлено письмо и появилась страница с уведомлением')
    def check_finish_reg_page_text(self):
        finish_reg_text_field = self.browser.find_element(*LocatorsMainPage.text_finish_page)
        finish_page_reg = finish_reg_text_field.text
        CommonChecker.check_field_equals(
            finish_page_reg,
            self.data.text_finish_page_reg,
            assertion_message="Произошла ошибка отсутствует либо не правельный текст на странице",
        )

    @allure.step("Нажать на кнопку Войти")
    def click_on_button_login(self):
        click_button_login = self.browser.find_element(*self.locators_by.button_login)
        click_button_login.click()

    @allure.step("Авторизация пользователя.")
    def authorization(self, email: str, password: str):
        self.click_on_the_email_field()
        self.enter_on_the_email_field(email=email)
        self.click_on_the_password_input_field()
        self.enter_password_in_pass_field_login(password=password)
        self.click_on_button_login()
