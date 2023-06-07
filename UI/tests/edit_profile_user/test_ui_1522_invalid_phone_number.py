import allure


from UI.test_framework.pages.personal_profile_pages.profile_general_information_page import PersonalAreaPage


@allure.id("1522")
@allure.title("Некорректный номер телефона")
def test_ui_1522_invalid_phone_number(browser_with_auth):
    # клик по кнопке редактировать
    PersonalAreaPage(browser_with_auth).click_edit_button()
    #редактирование номера телефона
    PersonalAreaPage(browser_with_auth).edit_phone_number_field(phone_number="123")
    #проверка, что номер телефона не корректне
    PersonalAreaPage(browser_with_auth).check_error_invalid_phone_number()
    # rk