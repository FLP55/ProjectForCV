import allure
import pytest

from test_framework.ui.locators.profile_pages_loc.cards_page_loc import LocatorsProfileCardsPage
from test_framework.ui.pages.base_pages.base_page import BasePage


class ProfileCardsPage(BasePage):
    locators_by = LocatorsProfileCardsPage

    @allure.step("Клик на кнопку 'Раскрыть/Скрыть'.")
    def click_on_button_expand_hide(self):
        pass

    @allure.step("Проверка отображения основных карт")
    def check_displaying_basic_cards(self):
        pass

