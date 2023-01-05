import allure

from test_framework.api.data.client.client_status import statuses_client
from test_framework.api.data.phones_cleint.all_phones import valid_phone_number_no_client
from test_framework.api.steps.steps_api import ApiSteps
from test_framework.helpers.main_checkers import CommonChecker


@allure.id("C5978275")
@allure.title("C5978275. Регистрация не клиента банка в приложении")
def test_api_c5978275_reg_no_client_bank() -> None:
    # Регистрация не клиента банка
    ApiSteps().add_new_user_no_client_with_check_status_code(phone=valid_phone_number_no_client)

    # Проверка получения пользователя по номеру телефона
    response_json = ApiSteps().get_all_information_client_by_phone(phone=valid_phone_number_no_client).json()

    # Проверка телефона пользователя
    CommonChecker.check_field_equals(
        response_json["mobilePhone"], valid_phone_number_no_client, assertion_message="Телефон не совпадает"
    )

    # Проверка статус клиента
    CommonChecker.check_field_equals(
        response_json["clientStatus"], statuses_client["not active"], assertion_message="Статус не совпадает"
    )
