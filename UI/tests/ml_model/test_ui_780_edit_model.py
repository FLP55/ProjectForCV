import allure

from UI.test_framework.pages.another_pages.ml_models_page import MlModels
from UI.test_framework.pages.personal_profile_pages.profile_general_information_page import PersonalAreaPage


@allure.id("780")
@allure.title("Редактирование модели")
def test_ui_780_edit_model(browser_with_auth):
    # клик на вкладку мл-модели
    PersonalAreaPage(browser_with_auth).click_ml_model()
    # клик по мл-модели
    MlModels(browser_with_auth).click_to_model()
    # клик по кнопке редактировать модель
    MlModels(browser_with_auth).click_edit_model()
    # Заполнение поля имя
    MlModels(browser_with_auth).input_field_name("Новая модель")
    # Заполнения поля тип
    MlModels(browser_with_auth).input_field_type("Новый тип")
    # Нажатие на кнопку сохранить
    MlModels(browser_with_auth).click_save_button()