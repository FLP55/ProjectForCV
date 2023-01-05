# import allure
#
# from test_framework.ui.locators.profile_main_page_loc import LocatorsProfileMainPage
# from test_framework.ui.pages.base_pages.base_page import BasePage
#
#
# class ProfileMainPage(BasePage):
#     locators_by = LocatorsProfileMainPage
#
#     @allure.step("Клик на линк пользователя.")
#     def open_profile_general_information_page(self):
#         profile_general_information_page = self.browser.find_element(
#             *self.locators_by.profile_general_information_page_locator
#         )
#         profile_general_information_page.click()
#
#     @allure.step("Клик на вкладку 'Карты'.")
#     def open_profile_cards_page(self):
#         profile_cards_page = self.browser.find_element(*self.locators_by.profile_cards_page_locator)
#         profile_cards_page.click()

