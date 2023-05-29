from typing import Any
from API.app_data.base_requests import BaseRequests
from API.test_data.data_url import MainURL


class RequestsForTestAPI:
    def __init__(self) -> None:
        self.request = BaseRequests()
        self.base_url = MainURL().get_url_from_dict("base_url")
        self.headers = self.request.headers
        self.cookies = self.request.cookies

    def reg_client(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/auth/register/", json=payload)

    def auth_user(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/auth/login/", cookies=self.cookies, json=payload)

    def logout_user(self) -> Any:
        return self.request.post(url=f"{self.base_url}/auth/logout/", cookies=self.cookies)

    def delete_users(self, payload: dict) -> Any:
        return self.request.delete(url=f"{self.base_url}/service/remove-users/", cookies=self.cookies, json=payload)

    def change_password(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/auth/reset-password-request/", json=payload)