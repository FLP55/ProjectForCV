from typing import Any, Union


class CommonChecker:
    default_message = "Некорректный статус код"

    @staticmethod
    def check_status_code_ok(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 200, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_400(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 400, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_500(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 500, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_404(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 404, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_201(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 201, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_200(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 200, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_202(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 202, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_204(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 204, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_401(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 401, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_field_equals(
            field: str, expected_value: Union[str, int], assertion_message: str = "Некорректное значение поля"
    ) -> None:
        assert field == expected_value, assertion_message

    @staticmethod
    def check_key_in_collection(
            key: str, collection: Union[list, dict], assertion_message: str = "Некорректное значение поля"
    ) -> None:
        assert key in collection, assertion_message

    @staticmethod
    def check_not_empty_response(r: Any, assertion_message: str = default_message) -> None:
        assert r is not None, assertion_message



