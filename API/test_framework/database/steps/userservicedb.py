from typing import Any

import allure

from API.test_framework.database.checkers.userservicedb import CheckerUserService
from API.test_framework.database.queries.userservicedb import QueriesUserService
from API.test_framework.helpers.main_checkers import CommonChecker


class StepsUserService:
    def __init__(self):
        self.queries = QueriesUserService()
        self.db_checker = CheckerUserService()

    def get_token_for_change_password(self, user_id):
        requests = self.queries.select_key_for_change_password(user_id=user_id)
        return requests

    def get_name_from_joint_user(self, user_id):
        requests = self.queries.select_name_from_joint_user(user_id=user_id)
        return requests

    def check_name_that_did_not_change(self, first_name, second_name):
        CommonChecker.check_field_equals(
            first_name, second_name,
            assertion_message="Имя не совпадает"
        )

    def get_id_ml_model(self, ml_name):
        requests = self.queries.select_id_from_ml_model(ml_name=ml_name)
        return requests