from typing import Any


class DataClient:
    @staticmethod
    def get_payload_for_registration_user(email: str, password: str, confirm_password: str) -> Any:
        return {
            "email": email,
            "password": password,
            "password_confirmation": confirm_password,
            "recaptcha": "random_str"
        }

    @staticmethod
    def get_payload_for_authorization_user(email: str, password: str) -> Any:
        return {
                "email": email,
                "password": password,
                "recaptcha": "random"
                }

    @staticmethod
    def get_payload_only_email(email: str) -> Any:
        return {
            "email": email
        }

    @staticmethod
    def get_payload_for_delete_data(email: str) -> Any:
        return {
            "emails": email
        }



