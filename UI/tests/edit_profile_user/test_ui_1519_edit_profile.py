import allure

from UI.test_framework.pages.personal_profile_pages.profile_general_information_page import PersonalAreaPage


@allure.id("1519")
@allure.title("Успешное редактирование")
def test_ui_1519_edit_profile(browser_with_auth):
    # клик на кнопку редактировать
    PersonalAreaPage(browser_with_auth).click_edit_button()
    # Редактирование поля Имя
    PersonalAreaPage(browser_with_auth).edit_name_field(name="Павел")
    # Редактирование поля фамилия
    PersonalAreaPage(browser_with_auth).edit_second_name_field(second_name="Тюрин")
    # Редактирование поля отчество
    PersonalAreaPage(browser_with_auth).edit_last_name_field(last_name="Олегович")
    # Редактирование поля номер телефона
    PersonalAreaPage(browser_with_auth).edit_phone_number_field(phone_number="9249134466")
    # Нажатие на кнопку сохранить
    PersonalAreaPage(browser_with_auth).click_button_confirm()
    # Проверка, что все сохранилось
    PersonalAreaPage(browser_with_auth).check_confirm_changes()