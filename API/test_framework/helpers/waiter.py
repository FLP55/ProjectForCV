import functools
import time
from typing import Any, Type

from API.test_framework.helpers.log import main_logger

logger = main_logger()


# Функция взаимодействует с assert и проверяет его на True/False
class WaitException(AssertionError):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


def checker_exception(step: Any) -> Any:

    step_name = step.__name__.split(".")[-1]

    @functools.wraps(step)
    def wrap(*args: Any, **kwargs: Any) -> Any:
        try:
            response = step(*args, **kwargs)
        except AssertionError as err:
            raise WaitException(f"Проверка {step_name}, завершилась неудачно: {str(err)}")

        return response

    return wrap


# Функция взаимодействует с кастомным классом WaitException и ждет пока результат выполнения метода будет True
def step_waiter(timeout: int = 0, wait_interval: int = 0, wait_exceptions: Type[BaseException] = WaitException) -> Any:
    def _wait(step: Any) -> Any:

        step_name = step.__name__.split(".")[-1]

        @functools.wraps(step)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            wait_until = int(time.time()) + timeout

            while wait_until > time.time():
                try:
                    return step(*args, **kwargs)
                except wait_exceptions:
                    logger.info(f"Waiting for {step_name}")
                    time.sleep(wait_interval)
            return step(*args, **kwargs)

        return wrapper

    return _wait
