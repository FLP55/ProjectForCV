import allure
import pytest

from test_framework.api.data.client.client_status import statuses_client
from test_framework.api.data.phones_cleint import all_phones as test_data
from test_framework.api.data.phones_cleint.all_phones import valid_phone_number_no_client
from test_framework.api.steps.steps_api import ApiSteps
from test_framework.helpers.main_checkers import CommonChecker


@allure.id("C5978422")
@allure.title("C5978422. Регистрация клиента банка в приложении")
@pytest.mark.skip
def test_api_c5978275_reg_no_client_bank() -> None:
    # Регистрация клиента банка в приложении Временно не работает в связи с отсутствием логики
    ApiSteps().add_new_client_with_check_status_code(phone=valid_phone_number_no_client)

    # Проверка получения пользователя по номеру телефона
    response_json = ApiSteps().get_all_information_client_by_phone(phone=test_data.valid_phone_number).json()

    # Проверка телефона пользователя
    CommonChecker.check_field_equals(
        response_json["mobilePhone"], test_data.valid_phone_number, assertion_message="Телефон не совпадает"
    )

    # Проверка статус клиента
    CommonChecker.check_field_equals(
        response_json["clientStatus"], statuses_client["active"], assertion_message="Статус не совпадает"
    )
