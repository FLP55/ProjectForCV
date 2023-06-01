from sqlalchemy import Boolean, Column, Integer, String

from API.test_framework.database.base import BaseModel


class JointUser(BaseModel):
    __tablename__ = "joint_user"

    id = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String)
    position = Column(String)
    phone = Column(String)
    is_business_admin = Column(Boolean)
    state = Column(String)
    account_id = Column(String)
    company_id = Column(String)
    created_at = Column(Integer)


class Company(BaseModel):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    INN = Column(Boolean)
    description = Column(Boolean)
    is_active = Column(Boolean)
    industry_id = Column(Integer)
    country = Column(String)
    region = Column(String)


class UserAccount(BaseModel):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    password = Column(String)
    email = Column(String)
    confirmed = Column(Boolean)
    is_active = Column(Boolean, nullable=True)
    is_staff = Column(Boolean)
    is_superuser = Column(Boolean)
    region = Column(String)


class AlliancesAlliance(BaseModel):
    __tablename__ = "alliances_alliance"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_closed = Column(Boolean)
    is_active = Column(Boolean)
    alliance_owner_id = Column(Integer)
    description = Column(String)
    industry_id = Column(Integer)


class AlliancesAllianceMlModels(BaseModel):
    __tablename__ = "alliances_alliance_ml_models"

    id = Column(Integer, primary_key=True)
    alliance_id = Column(Integer)
    machinelearningmodel_id = Column(Integer)


class MlModels(BaseModel):
    __tablename__ = "ml_models"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    model_type = Column(String)
    description = Column(String)
    task = Column(String)
    tags = Column(String)
    author_id = Column(String)
    size = Column(String)
    owner_id = Column(Integer)

class Tokens(BaseModel):
    __tablename__ = "tokens"
    created_at = Column(String)
    key = Column(String, primary_key=True)
    user_id_id = Column(Integer)
