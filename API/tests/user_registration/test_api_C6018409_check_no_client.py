# import allure
# import pytest
#
# from test_framework.api.data.client.client import statuses_client
# from test_framework.api.data.phones_cleint.all_phones import phone_no_client
# from test_framework.api.steps.steps_api import ApiSteps
# from test_framework.helpers.main_checkers import CommonChecker
#
#
# @allure.id("C6018409")
# @allure.title("C6018409. Проверка регистрации пользователя (статус NOT_CLIENT)")
# @pytest.skip
# def test_api_c6018408_check_status() -> None:
#
#     # Проверка получения пользователя по номеру телефона
#     response_json = ApiSteps().get_all_information_client_by_phone(phone=phone_no_client).json()
#
#     # Проверка телефона пользователя
#     CommonChecker.check_field_equals(
#         response_json["mobilePhone"], phone_no_client, assertion_message="Телефон не совпадает"
#     )
#
#     # Проверка статус клиента
#     CommonChecker.check_field_equals(
#         response_json["clientStatus"], statuses_client["not client"], assertion_message="Статус не совпадает"
#     )
