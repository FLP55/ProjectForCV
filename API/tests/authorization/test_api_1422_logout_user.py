import allure

from API.test_framework.steps.steps_api import ApiSteps


@allure.id("1422")
@allure.title("Логаут пользователя")
def test_api_1422_logout_user(auth_user):
    ApiSteps().logout_user()