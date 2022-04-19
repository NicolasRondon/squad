from sqlmodel import SQLModel

from jokes_api.database import engine
from jokes_api.models import Joke  # noqa


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
