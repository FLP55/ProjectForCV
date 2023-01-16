from typing import Any

from API.app_data.base_requests import BaseRequests
from API.test_data.data_url import MainURL

main_headers = {"Fingerprint": "xxx"}


class RequestsForTestSait:
    def __init__(self) -> None:
        self.request = BaseRequests()
        self.base_url = MainURL().get_url_from_dict("base_url")
        self.headers = main_headers

    def get_all_information_from_sait(self, valid_phone_number_no_client: str) -> Any:
        return self.request.get(url=f"{self.base_url}/api/v1/registration?mobilePhone={valid_phone_number_no_client}")

    def reg_no_client(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/api/v1/registration/user-profile/new/", json=payload)

    def reg_client(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/register/", json=payload)

    def get_phone_number_by_passport(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/api/v1/security/session", json=payload)

    def get_verification_code_by_phone(self, phone: str) -> Any:
        return self.request.get(url=f"{self.base_url}/api/v1/security/session?receiver={phone}")

    def get_authorization_token(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/api/v1/login/", headers=self.headers, json=payload)

    def update_email(self, client_id: str, payload: dict) -> Any:
        return self.request.patch(
            url=f"{self.base_url}/api/v1/user/settings/email?clientId={client_id}", headers=self.headers, json=payload
        )

    def update_subscription_status(self, client_id: str, payload: dict) -> Any:
        return self.request.patch(
            url=f"{self.base_url}/api/v1/user/settings/notifications/email?clientId={client_id}",
            headers=self.headers,
            json=payload,
        )

    def changing_email_with_wrong_address(self, client_id: str, payload: dict, headers) -> Any:
        return self.request.patch(
            url=f"{self.base_url}/api/v1/user/settings/email?clientId={client_id}", headers=headers, json=payload
        )

    def get_set_new_password_by_phone(self, phone_number: str, payload: dict) -> Any:
        return self.request.patch(
            url=f"{self.base_url}/api/v1/login/password?mobilePhone={phone_number}", headers=self.headers, json=payload
        )

    def get_info_about_notification_by_id(self, id_client: str) -> Any:
        return self.request.get(
            url=f"{self.base_url}api/v1/user/settings/notifications/all?clientId={id_client}", headers=self.headers
        )

    def get_info_about_notification_by_invalid_id(self, id_client: str) -> Any:
        return self.request.get(url=f"{self.base_url}api/v1/user/settings/notifications/all?clientId={id_client}")

    def logout_user_token(self) -> Any:
        return self.request.get(url=f"{self.base_url}/api/v1/logout", headers=self.headers)

    def update_client_status_in_Active(self, status: str) -> Any:
        return self.request.patch(
            url=f"{self.base_url}/api/v1/test/change-client-status/?status={status}", headers=self.headers
        )
