from typing import Any

import allure

from app_data.api.requests_for_saite.requests import RequestsForTestSait
from test_data.api.api_data import DataClient
from test_framework.api.api_checkers.checkers import CheckersApi
from test_framework.helpers.main_checkers import CommonChecker


class ApiSteps:
    def __init__(self) -> None:
        self.request = RequestsForTestSait()
        self.checker = CheckersApi()
        self.data = DataClient()


