import allure

from API.test_framework.database.steps.userservicedb import StepsUserService
from UI.test_framework.pages.personal_profile_pages.profile_general_information_page import PersonalAreaPage


@allure.id("1523")
@allure.title("Отмена изменений")
def test_ui_1523_cancel_changes(browser_with_auth):
    #получение данных из бд
    name_from_bd = StepsUserService().get_token_for_change_password(user_id="11")[0][0]
    # клик на кнопку редактировать
    PersonalAreaPage(browser_with_auth).click_edit_button()
    # Редактирование поля Имя
    PersonalAreaPage(browser_with_auth).edit_name_field(name="Олег")
    # Редактирование поля фамилия
    PersonalAreaPage(browser_with_auth).edit_second_name_field(second_name="Тюрин")
    # Редактирование поля отчество
    PersonalAreaPage(browser_with_auth).edit_last_name_field(last_name="Павлович")
    # Редактирование поля номер телефона
    PersonalAreaPage(browser_with_auth).edit_phone_number_field(phone_number="3333333333")
    # Нажатие на кнопку отмена
    PersonalAreaPage(browser_with_auth).click_cancel_button()
    # повторное полученние данных
    second_name_from_bd = StepsUserService().get_token_for_change_password(user_id="11")[0][0]
    # Проверка, что данные не изменились
    StepsUserService().check_name_that_did_not_change(first_name=name_from_bd, second_name=second_name_from_bd)