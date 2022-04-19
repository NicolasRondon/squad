import requests
from constants import API_URL

from jokes_api.modules.base.abstract import GetContentJokeAPI, Service
from jokes_api.modules.base.entities import ResultJoke


class DadJokesService(Service):
    """
    Class to get info and content from dad jokes api
    """

    def __init__(self):
        self.api_url = API_URL
        self.client = requests.Session()
        self.retry(
            status_forcelist=(504, 429),
            method_whitelist=["GET"],
            backoff_factor=2,
            total_retries=2,
        )

    @Service.response_exception(message="Error getting random joke from dad jokes")
    def get_joke(self) -> dict:
        """
        Get a random dad  joke
        """
        response = self.client.get(self.api_url, headers={"Accept": "application/json"})
        response = response.json()
        return response


class DadJokesInstance(GetContentJokeAPI):
    def check_connection(self) -> bool:
        dad_jokes_service = DadJokesService()
        try:
            response = dad_jokes_service.get_joke()
        except Exception:
            return False
        else:
            if not response:
                return False
            return response.get("success", False)

    def get_random_joke(self) -> ResultJoke:
        dad_jokes_service = DadJokesService()
        joke_data = dad_jokes_service.get_joke()
        joke_id = joke_data.get("id", None)
        joke_text = joke_data.get("joke", None)
        response = ResultJoke(id_joke=joke_id, joke=joke_text)
        return response


a = DadJokesInstance().get_random_joke()
print(a)
