from typing import Any, Union

from sqlalchemy import bindparam, update

from API.test_framework.database.db.user_service import UserServiceDB
from API.test_framework.database.orm.base_config_db import BaseDB
from API.test_framework.database.orm.usersevicedb import UserAccount, JointUser, Tokens, MlModels


class QueriesUserService:
    def __init__(self, db: BaseDB = None):
        self.db = db or UserServiceDB()

    def select_key_for_change_password(self, user_id) -> Union[Tokens, Any]:
        with self.db.create_session() as session:
            return session.query(Tokens.key).filter(Tokens.user_id_id == user_id)

    def select_name_from_joint_user(self, user_id) -> Union[JointUser, Any]:
        with self.db.create_session() as session:
            return session.query(JointUser.first_name).filter(JointUser.id == user_id)

    def select_id_from_ml_model(self, ml_name) -> Union[MlModels, Any]:
        with self.db.create_session() as session:
            return session.query(MlModels.id).filter(MlModels.name == ml_name)