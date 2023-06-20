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

    @staticmethod
    def get_payload_for_confirm_change_password(token: str, password: str, confirm_password: str) -> Any:
        return {
            "token": token,
            "password": password,
            "password_confirmation": confirm_password
        }

    @staticmethod
    def get_payload_for_changes_data_about_user(first_name: str, last_name: str, second_name: str, phone_number: str):
        return {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": second_name,
            "position": "Сотрудник",
            "phone": phone_number
        }

    @staticmethod
    def get_payload_for_create_model(id: str, name: str, model_type: str, description: str):
        return {
            "id": id,
            "name": name,
            "model_type": model_type,
            "task": "1",
            "description": description,
            "category": "2"
        }

    @staticmethod
    def get_payload_for_edit_model(name: str, model_type: str, description: str):
        return {
            "name": name,
            "model_type": model_type,
            "description": description,
        }