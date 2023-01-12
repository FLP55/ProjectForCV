from typing import Any

from API.test_framework.database.checkers.userservicedb import CheckerUserService
from API.test_framework.database.queries.userservicedb import QueriesUserService


class StepsUserService:
    def __init__(self):
        self.queries = QueriesUserService()
        self.db_checker = CheckerUserService()

    def check_user_id(self, get_db_session: Any, user_ud: str = None) -> None:
        return self.queries.select_all_data_from_table(get_db_session)

