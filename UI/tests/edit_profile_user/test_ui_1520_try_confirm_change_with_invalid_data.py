import allure

from UI.test_framework.locators.profile_main_page_loc import LocatorsProfileMainPage
from UI.test_framework.pages.personal_profile_pages.profile_general_information_page import PersonalAreaPage


@allure.id("1520")
@allure.title("Попытка ввода чисел в поля для букв")
def test_ui_1520_try_confirm_change_with_invalid_data(browser_with_auth):
    # клик на кнопку редактировать
    PersonalAreaPage(browser_with_auth).click_edit_button()
    # Редактирование поля Имя
    PersonalAreaPage(browser_with_auth).edit_name_field(name="12345678")
    # Редактирование поля фамилия
    PersonalAreaPage(browser_with_auth).edit_second_name_field(second_name="12345678")
    # Редактирование поля отчество
    PersonalAreaPage(browser_with_auth).edit_last_name_field(last_name="12345678")
    # Проверка наличие ошибок под полями
    PersonalAreaPage(browser_with_auth).check_error_invalid_data(
        LocatorsProfileMainPage().error_invalid_data_field_last_name
    )
    PersonalAreaPage(browser_with_auth).check_error_invalid_data(
        LocatorsProfileMainPage().error_invalid_data_field_name
    )
    PersonalAreaPage(browser_with_auth).check_error_invalid_data(
        LocatorsProfileMainPage().error_invalid_data_field_second_name
    )
    #Нажатие на кнопку сохранить изменения
    PersonalAreaPage(browser_with_auth).click_button_confirm()
    # Проверка, что изменения не сохранились
    PersonalAreaPage(browser_with_auth).check_clickable_button_confirm()