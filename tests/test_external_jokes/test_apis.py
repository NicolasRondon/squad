from jokes_api.modules.jokes.chuck.api import ChuckJokesInstance, ChuckJokesService
from jokes_api.modules.jokes.dad.api import DadJokesInstance, DadJokesService


def test_chuck_jokes():
    srvice = ChuckJokesService()
    data = srvice.get_joke()
    assert "id" in data.keys()


def test_dad_jokes():
    srvice = DadJokesService()
    data = srvice.get_joke()
    assert "id" in data.keys()


def test_dad_instance_connection():
    instance = DadJokesInstance()
    connection = instance.check_connection()
    assert connection is True


def test_chuck_instance_connection():
    instance = ChuckJokesInstance
    connection = instance.check_connection()
    assert connection is True
