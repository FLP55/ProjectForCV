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
    is_active = Column(Boolean)
    is_staff = Column(Boolean)
    is_superuser = Column(Boolean)
    region = Column(String)


class AlliancesAlliance(BaseModel):
    __tablename__ = "alliances_alliance"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_closed = Column(String)
    is_active = Column(Boolean)
    is_staff = Column(Boolean)
    is_superuser = Column(Boolean)
    region = Column(String)


class UserProfile(BaseModel):
    __tablename__ = "db_user_profile"

    id = Column(Integer, primary_key=True)
    id_client = Column(String)
    security_question = Column(String)
    security_answer = Column(String)


class Verification(BaseModel):
    __tablename__ = "db_verification"

    id = Column(Integer, primary_key=True)
    id_contact = Column(String)
    sms_verification_code = Column(String)
