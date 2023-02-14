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
    def get_payload_for_delete_users(emails: str) -> Any:
        return {
            "emails": emails
        }

    @staticmethod
    def get_payloda_register_complition() -> Any:
        return {
                "first_name": "Денис",
                "last_name": "Денисов",
                "middle_name": "Юрьевич2",
                "company": "Тестовая компания",
                "position": "QA",
                "phone": "800555777",
                "is_business_admin": "False"
            }



