import functools
from abc import ABC, abstractmethod

import requests

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
