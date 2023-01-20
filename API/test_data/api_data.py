import uuid


class DataClient:
    @staticmethod
    def get_payload_for_registration_user(email: str, password: str, confirm_password: str) -> dict:
        return {
            "email": email,
            "password": password,
            "password_confirmation": confirm_password,
            "recaptcha": "random_str"
        }

    @staticmethod
    def get_payload_for_authorization_user(email: str, password: str) -> dict:
        return {
                "email": email,
                "password": password,
                "recaptcha": "random"
                }

