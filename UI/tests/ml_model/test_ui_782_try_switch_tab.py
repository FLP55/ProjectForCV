import allure

from UI.test_framework.pages.another_pages.ml_models_page import MlModels
from UI.test_framework.pages.personal_profile_pages.profile_general_information_page import PersonalAreaPage


@allure.id("782")
@allure.title("Смена вкладки")
def test_ui_782_try_switch_tab(browser_with_auth):
    # клик на вкладку мл-модели
    PersonalAreaPage(browser_with_auth).click_ml_model()
    # клик по мл-модели
    MlModels(browser_with_auth).click_to_model()
    # клик по кнопке редактировать модель
    MlModels(browser_with_auth).click_edit_model()
    # Переход на вкладку и поддтверждение, так же проверка успешности
    MlModels(browser_with_auth).try_switch_tab()