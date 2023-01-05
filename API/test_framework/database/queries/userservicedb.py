from typing import Any

from test_framework.database.orm.usersevicedb import Client


class QueriesUserService:

    @staticmethod
    def select_all_data_from_table(get_db_session: Any):
        return get_db_session.query(Client.id).first()

