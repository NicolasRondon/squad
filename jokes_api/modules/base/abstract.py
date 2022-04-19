import functools
from abc import ABC, abstractmethod
from typing import List, Tuple

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

import settings
from jokes_api.modules.base.entities import ResultJoke
from jokes_api.modules.base.exceptions import JokeServiceError


class GetContentJokeAPI(ABC):
    """
    Abstract Class to get jokes from apis
    """

    @abstractmethod
    def get_random_joke(self) -> ResultJoke:
        """Get a random joke from api"""
        pass

    @abstractmethod
    def check_connection(self) -> bool:
        """Checks if the connection to the joke service  is successfull
        Returns:
            bool: true if the connection with the integration is successfull
        """
        pass


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = settings.DEFAULT_REQUESTS_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


class Service:
    """
    Class base to use on service jokes
    """

    @classmethod
    def _raise_error(
        cls, error_obj: requests.exceptions.RequestException, service: str
    ):
        status_code = None
        json_response = None

        if error_obj.response:
            status_code = error_obj.status_code
            try:
                json_response = error_obj.response.json()
            except Exception:
                json_response = None

        raise JokeServiceError(
            error=str(error_obj),
            response=json_response,
            status_code=status_code,
            service=service,
        ) from error_obj

    @classmethod
    def response_exception(cls, message):
        def outer(func):
            @functools.wraps(func)
            def inner(*args, **kwargs):
                try:
                    response = func(*args, **kwargs)
                    return response
                except requests.exceptions.RequestException as e:
                    cls._raise_error(e, message)

            return inner

        return outer

    def retry(
        self,
        status_forcelist: Tuple[int, int],
        allowed_methods: List[str],
        backoff_factor: int,
        total_retries: int,
    ):
        """
        Function to retry an endpoint request
        :param status_forcelist: A set of integer HTTP status codes that we should force a retry on.
        :param allowed_methods: White list for HTTP Methods
        :param backoff_factor: A backoff factor to apply between attempts after the second try
        (most errors are resolved immediately by a second try without a
        delay).
        :param total_retries: Total of retries
        :return:
        """
        retry_strategy = Retry(
            total=total_retries,
            status_forcelist=status_forcelist,
            allowed_methods=allowed_methods,
            backoff_factor=backoff_factor,
        )

        adapter = TimeoutHTTPAdapter(timeout=7, max_retries=retry_strategy)
        self.client.mount("https://", adapter=adapter)
        self.client.mount("http://", adapter=adapter)
