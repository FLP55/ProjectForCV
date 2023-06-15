import allure

from UI.test_framework.pages.another_pages.ml_models_page import MlModels
from UI.test_framework.pages.personal_profile_pages.profile_general_information_page import PersonalAreaPage


@allure.id("781")
@allure.title("Редактирование модели c пробелами")
def test_ui_781_try_edit_model_with_space(browser_with_auth):
    # клик на вкладку мл-модели
    PersonalAreaPage(browser_with_auth).click_ml_model()
    # клик по мл-модели
    MlModels(browser_with_auth).click_to_model()
    # клик по кнопке редактировать модель
    MlModels(browser_with_auth).click_edit_model()
    # Заполнение поля имя
    MlModels(browser_with_auth).input_field_name("   ")
    # Заполнения поля тип
    MlModels(browser_with_auth).input_field_type("   ")
    # Нажатие на кнопку сохранить
    MlModels(browser_with_auth).click_save_button()