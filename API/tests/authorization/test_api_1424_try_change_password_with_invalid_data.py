import allure


from API.test_framework.steps.steps_api import ApiSteps


@allure.id("1424")
@allure.title("Попытка отправки запроса на смену пароля с неверными данными")
def test_api_1424_try_change_password_with_invalid_data():
    ApiSteps().check_status_for_change_password_with_invalid_data(email="pavelMail.ru")