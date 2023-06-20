from typing import Any
from API.app_data.base_requests import BaseRequests
from API.test_data.data_url import MainURL
from UI.test_framework.data.for_tests.file_for_create_ml_models import config_path


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

    def confirm_password(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/auth/reset-password-confirm/", json=payload)

    def get_user_info(self) -> Any:
        return self.request.get(url=f"{self.base_url}/user/", cookies=self.cookies)

    def change_user_info(self, payload: dict) -> Any:
        return self.request.patch(url=f"{self.base_url}/user/", cookies=self.cookies, json=payload)

    def delete_ml_models(self, id_ml: str) -> Any:
        return self.request.delete(url=f"{self.base_url}/mlmodels/{id_ml}/", cookies=self.cookies)

    def create_model(self, payload: dict) -> Any:
        return self.request.post(
            url=f"{self.base_url}/mlmodels/", files={"model_file": config_path}, json=payload, cookies=self.cookies
        )

    def edit_model(self, payload: dict, id_ml) -> Any:
        return self.request.patch(url=f"{self.base_url}/mlmodels/{id_ml}/", json=payload, cookies=self.cookies)