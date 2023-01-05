# import allure
#
# from test_data.ui.url_data import MAIN_PAGE_URL, PRIVACY_POLICY
# from test_framework.helpers.main_checkers import CommonChecker
# from test_framework.ui.locators.registration_page_loc import LocatorsRegistrationPage
# from test_framework.ui.pages.base_pages.base_page import BasePage
#
#
# class RegistrationPage(BasePage):
#     locators_by = LocatorsRegistrationPage
#
#     @allure.step("Клик на поле ввода номера телефона.")
#     def check_hint_enter_number_after_click_on_phone_field(self):
#         phone_field = self.browser.find_element(*self.locators_by.field_phone_locator)
#         phone_field.click()
#
#         text_enter_number = self.browser.find_element(*self.locators_by.text_enter_number_locator).text
#         CommonChecker.check_field_equals(
#             text_enter_number, "Введите номер телефона", assertion_message="Тексты подсказок не совпадают"
#         )


