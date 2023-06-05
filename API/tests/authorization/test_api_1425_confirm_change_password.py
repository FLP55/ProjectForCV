import allure

from API.test_framework.data.email.real_email import password
from API.test_framework.database.steps.userservicedb import StepsUserService
from API.test_framework.steps.steps_api import ApiSteps


@allure.id("1425")
@allure.title("Подтверждение смены пароля")
def test_api_1425_confirm_change_password():
    #Получение токена для смены пароля
    token = StepsUserService().get_token_for_change_password(user_id="12")[0][0]
    #Смена пароля
    ApiSteps().confirm_change_password(token=token, password=password, confirm_password=password)