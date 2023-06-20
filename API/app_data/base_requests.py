from typing import Any

import requests
from requests import Response

from API.test_framework.helpers.log import main_logger
from API.test_framework.helpers.report import allure_attach_response

headers = {"Content-Type": "application/json"}
global_cookies = dict()
class BaseRequests:
    def __init__(self) -> None:
        self.headers = headers
        self.logger = main_logger()
        self.cookies = global_cookies
    def get(self, url: str, cookies: str = None) -> Response:
        return self._api_call("GET", url=url, cookies=cookies)

    def patch(self, url: str, json: dict, cookies: str = None) -> Response:
        return self._api_call("PATCH", url=url, json=json, cookies=cookies)

    def post(self, url: str, json: dict = None, cookies: str = None, files: dict = None) -> Response:
        return self._api_call("POST", url=url, json=json, cookies=cookies, files=files)

    def put(self, url: str, json: dict = None) -> Response:
        return self._api_call("PUT", url=url, json=json)

    def delete(self, url: str, cookies: str = None, json: dict = None) -> Response:
        return self._api_call("DELETE", url=url, cookies=cookies, json=json)

    def _api_call(self, method: Any, url: str, json: dict = None, cookies: str = None) -> Any:
        try:
            return self._request(method, url, json=json, cookies=cookies)
        except Exception as error:
            self.logger.error(f"***<ERROR>: {error}\n ***")
        return None

    @allure_attach_response
    def _request(self, method: Any, url: str, json: dict = None, cookies: str = None) -> Response:
        return requests.request(method, url, json=json, cookies=cookies)
