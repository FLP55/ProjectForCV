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

