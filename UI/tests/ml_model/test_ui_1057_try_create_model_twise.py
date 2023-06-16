import time

import allure

from UI.test_framework.data.user_data import description
from UI.test_framework.pages.another_pages.create_model_page import CreateMlModel
from UI.test_framework.pages.another_pages.ml_models_page import MlModels
from UI.test_framework.pages.personal_profile_pages.profile_general_information_page import PersonalAreaPage


@allure.id("1057")
@allure.title("Создание ML модели в ЛК с валидными данными повторно, проверка на уникальность")
def test_ui_1057_try_create_model_twise(browser_with_delete_model):
    #клик на вкладку мл-модели
    PersonalAreaPage(browser_with_delete_model).click_ml_model()
    #клик на кнопку создать модель
    MlModels(browser_with_delete_model).click_button_create_new_model()
    # заполение поля имя
    CreateMlModel(browser_with_delete_model).input_field_name(name="Модель для автотестов12")
    # заполение поля тип задач
    CreateMlModel(browser_with_delete_model).input_field_type()
    # заполение поля категория
    CreateMlModel(browser_with_delete_model).input_category_field()
    # заполение поля тип модели
    CreateMlModel(browser_with_delete_model).input_field_type_ml_model(type="Модель для автотестов")
    # заполение поля описание
    CreateMlModel(browser_with_delete_model).input_field_description(description=description)
    # выбор тега
    CreateMlModel(browser_with_delete_model).click_tag()
    # добавление файла
    CreateMlModel(browser_with_delete_model).add_file()
    # клик на кнопку добавить
    CreateMlModel(browser_with_delete_model).click_button_add()
    # клик на кнопку создать модель
    MlModels(browser_with_delete_model).click_button_create_new_model()
    # заполение поля имя
    CreateMlModel(browser_with_delete_model).input_field_name(name="Модель для автотестов12")
    # заполение поля тип задач
    CreateMlModel(browser_with_delete_model).input_field_type()
    # заполение поля категория
    CreateMlModel(browser_with_delete_model).input_category_field()
    # заполение поля тип модели
    CreateMlModel(browser_with_delete_model).input_field_type_ml_model(type="Модель для автотестов")
    # заполение поля описание
    CreateMlModel(browser_with_delete_model).input_field_description(description=description)
    # выбор тега
    CreateMlModel(browser_with_delete_model).click_tag()
    # добавление файла
    CreateMlModel(browser_with_delete_model).add_file()
    # клик на кнопку добавить
    CreateMlModel(browser_with_delete_model).click_button_add()
    # проверка, что модель не создается
    CreateMlModel(browser_with_delete_model).check_error_about_repeated_name()