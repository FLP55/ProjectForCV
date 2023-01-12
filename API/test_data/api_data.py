import uuid


class DataClient:
    @staticmethod
    def get_payload_for_no_client(phone_number_no_client: str) -> dict:
        return {
            "mobilePhone": phone_number_no_client,
            "password": "Qwerty5",
            "securityQuestion": "cat name",
            "securityAnswer": "vasika",
            "email": "denis1488@mail.ru",
            "firstName": "Denis",
            "lastName": "Kotov",
            "passportNumber": "SN-121-000-100",
            "countryOfResidence": "RU",
            "ExpiryDate": "2022-09-28",
            "middleName": "Yurievich",
        }

    @staticmethod
    def get_payload_for_client(phone_number: str) -> dict:
        return {
            "mobilePhone": phone_number,
            "id": str(uuid.uuid4()),
            "password": "Qwerty55",
            "securityQuestion": "cat name",
            "securityAnswer": "niki",
            "email": f"{phone_number}@mail.ru",
        }

    @staticmethod
    def get_email_for_change_no_valid(expected_email: str) -> dict:
        return {"newEmail": expected_email}

    @staticmethod
    def get_password_for_change_valid(expected_password: str) -> dict:
        return {"newPassword": expected_password}

    @staticmethod
    def get_email_for_change() -> dict:
        return {"newEmail": "maria123@mail.ru"}

    @staticmethod
    def activate_status() -> dict:
        return {"notificationStatus": True}

    @staticmethod
    def deactivate_status() -> dict:
        return {"notificationStatus": False}

    @staticmethod
    def get_data_passport_number(passport_number: str) -> dict:
        return {"passportNumber": passport_number}

    @staticmethod
    def get_payload_for_authorization_with_phone(phone_number: str, password: str) -> dict:
        return {"login": phone_number, "password": password, "type": "PHONE_NUMBER"}

    @staticmethod
    def get_payload_for_authorization_with_passport(passport_number: str) -> dict:
        return {"login": passport_number, "password": "Qwerty5", "type": "PASSPORT_NUMBER"}

    @staticmethod
    def get_payload_for_authorization_with_invalid_data(data: dict) -> dict:
        return {"login": data["login"], "password": data["password"], "type": data["type"]}

    @staticmethod
    def get_payload_for_authorization_with_password(phone_number: str, password: str) -> dict:
        return {"login": phone_number, "password": password, "type": "PHONE_NUMBER"}
