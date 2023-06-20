import allure

from API.test_framework.steps.steps_api import ApiSteps


@allure.id("1587")
@allure.title("Попытка создания моделей, с данными ввиде пробелов")
def test_api_1587_try_create_model_with_space(auth_user_and_delete_model):
    ApiSteps().check_unsuccess_create_model(id="   ", name="   ", model_type="  ", description="   ")