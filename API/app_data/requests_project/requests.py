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

    def login_check(self):
        return self.request.get(url=f"{self.base_url}/auth/login_check/", cookies=self.cookies)

    def logout_user(self) -> Any:
        return self.request.post(url=f"{self.base_url}/logout/", cookies=self.cookies)

    def delete_users(self, payload: dict) -> Any:
        return self.request.delete(url=f"{self.base_url}/service/remove-users/", cookies=self.cookies, json=payload)

    def register_completion(self, payload: Any) -> Any:
        return self.request.post(url=f"{self.base_url}/user/completion/", json=payload)

    def get_details_about_ml_model(self, id_model):
        return self.request.get(url=f"{self.base_url}/mlmodels/{id_model}", cookies=self.cookies)