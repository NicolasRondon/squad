import os

from sqlmodel import Session, create_engine

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
sqlite_file_name = "database.db"
sqlite_url = "sqlite:///" + os.path.join(BASE_DIR, sqlite_file_name)
engine = create_engine(sqlite_url, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
