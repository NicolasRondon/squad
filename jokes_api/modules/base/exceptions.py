from typing import Any, Optional

from jokes_api.modules.base import constants


class JokeError(Exception):
    def __init__(
        self,
        msg: str,
        code: int,
        error: Optional[Any] = None,
        extra: Optional[dict] = None,
    ) -> None:
        self.msg = msg
        self.code = code
        self.error = error
        self.extra = extra
        super().__init__(msg, error, extra)


class JokeServiceError(JokeError):
    code = constants.JOKE_SERVICE_ERROR_CODE

    def __init__(
        self, error: Any, response: dict, status_code: int, service: str
    ) -> None:
        super().__init__(
            msg=constants.ERROR_MESSAGES[self.code],
            code=self.code,
            error=error,
            extra={
                "response": response,
                "status_code": status_code,
                "service": service,
            },
        )
