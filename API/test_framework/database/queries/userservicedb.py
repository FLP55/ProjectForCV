from typing import Any, Union

from sqlalchemy import bindparam, update

from API.test_framework.database.db.user_service import UserServiceDB
from API.test_framework.database.orm.base_config_db import BaseDB
from API.test_framework.database.orm.usersevicedb import UserAccount, JointUser


class QueriesUserService:
    def __init__(self, db: BaseDB = None):
        self.db = db or UserServiceDB()

    def select_all_data_from_table_user_account(self) -> Union[UserAccount, Any]:
        with self.db.create_session() as session:
            return session.query(UserAccount.id).first()

    def select_id_user_from_user_account(self) -> Union[UserAccount, Any]:
        with self.db.create_session() as session:
            return session.query(UserAccount.id).filter(UserAccount.email == "autotestsmokeU@mail.ru")

    def confirm_email_user(self, user: str) -> Union[UserAccount, Any]:
        with self.db.create_session() as session:
            return session.execute(update(UserAccount).where(
                UserAccount.email == user).values(confirmed=True))


