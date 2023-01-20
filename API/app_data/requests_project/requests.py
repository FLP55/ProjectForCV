from typing import Any

from API.app_data.base_requests import BaseRequests
from API.test_data.data_url import MainURL

main_headers = {"Fingerprint": "xxx"}


class RequestsForTestSait:
    def __init__(self) -> None:
        self.request = BaseRequests()
        self.base_url = MainURL().get_url_from_dict("base_url")
        self.headers = main_headers

    def reg_client(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/register/", json=payload)

    def auth_user(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}/login/", json=payload)
