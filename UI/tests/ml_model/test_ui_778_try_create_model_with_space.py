import allure

from UI.test_framework.data.for_tests.file_for_create_ml_models import config_path
from UI.test_framework.pages.another_pages.create_model_page import CreateMlModel
from UI.test_framework.pages.another_pages.ml_models_page import MlModels
from UI.test_framework.pages.personal_profile_pages.profile_general_information_page import PersonalAreaPage


@allure.id("778")
@allure.title("Попытка создания ML с пустыми полями")
def test_ui_779_check_fields(browser_with_delete_model):
    #клик на вкладку мл-модели
    PersonalAreaPage(browser_with_delete_model).click_ml_model()
    #клик на кнопку создать модель
    MlModels(browser_with_delete_model).click_button_create_new_model()
    # заполение поля имя
    CreateMlModel(browser_with_delete_model).input_field_name(name="   ")
    # заполение поля тип задач
    CreateMlModel(browser_with_delete_model).input_field_type()
    # заполение поля категория
    CreateMlModel(browser_with_delete_model).input_category_field()
    # заполение поля тип модели
    CreateMlModel(browser_with_delete_model).input_field_type_ml_model(type="    ")
    # заполение поля описание
    CreateMlModel(browser_with_delete_model).input_field_description(description="   ")
    # добавление файла
    CreateMlModel(browser_with_delete_model).add_file(file_path=config_path)
    # клик на кнопку добавить
    CreateMlModel(browser_with_delete_model).check_button_continue_active()