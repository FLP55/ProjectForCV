import allure

from API.test_framework.data.email.real_email import id_model, name_model, description
from API.test_framework.steps.steps_api import ApiSteps


@allure.id("1591")
@allure.title("Редактирование модели граничные значения")
def test_api_1591_try_edit_model_with_boundary_data(auth_user_and_delete_model):
    ApiSteps().check_success_create_model(id=id_model, name=name_model, model_type=name_model, description=description)
    ApiSteps().check_un_success_edit_model(id_ml=id_model, name="1", model_type="1", description=description)
    ApiSteps().check_un_success_edit_model(
        id_ml=id_model, name=description, model_type=description, description=description
    )