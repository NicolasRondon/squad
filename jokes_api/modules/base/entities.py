from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class ResultJoke(BaseModel):
    icon: Optional[str]
    id_joke: str
    joke: str
    url: Optional[str]
    type_joke: str


class JokeBase(SQLModel):
    icon: Optional[str]
    joke: str
    url: Optional[str]


class Joke(JokeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class JokeCreate(JokeBase):
    pass


class JokeRead(JokeBase):
    id: int


class JokeUpdate(SQLModel):
    icon: Optional[str]
    joke: str
    url: Optional[str]
