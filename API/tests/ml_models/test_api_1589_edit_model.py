import allure

from API.test_framework.data.email.real_email import id_model, name_model, description
from API.test_framework.steps.steps_api import ApiSteps


@allure.id("1589")
@allure.title("Редактирование модели валидное")
def test_api_1589_edit_model(auth_user_and_delete_model):
    ApiSteps().check_success_create_model(id=id_model, name=name_model, model_type=name_model, description=description)
    ApiSteps().check_success_edit_model(id_ml=id_model, name=name_model, model_type=name_model, description=description)