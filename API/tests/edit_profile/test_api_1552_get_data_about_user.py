import allure

from API.test_framework.steps.steps_api import ApiSteps


@allure.id("1552")
@allure.title("получение данных о пользователе")
def test_api_1552_get_data_about_user(auth_user):
    ApiSteps().get_data_about_user()