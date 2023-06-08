import allure

from API.test_framework.steps.steps_api import ApiSteps


@allure.id("1554")
@allure.title("Редактирование данных")
def test_api_1554_edit_profile(auth_user):
    ApiSteps().edit_profile(first_name="Павел", last_name="Тюрин", second_name="Олегович", phone_number="9139995633")