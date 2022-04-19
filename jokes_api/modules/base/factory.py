from typing import Dict, Type

from jokes_api.modules.base.abstract import GetContentJokeAPI

from ..jokes.chuck.api import ChuckJokesInstance
from ..jokes.dad.api import DadJokesInstance
from .constants import CHUCK, DAD

mapper: Dict[str, Type[GetContentJokeAPI]] = {
    CHUCK: ChuckJokesInstance,
    DAD: DadJokesInstance,
}


def jokes_factory(
    integration_slug: str,
) -> GetContentJokeAPI:
    joke_instance = mapper.get(integration_slug)
    return joke_instance()
