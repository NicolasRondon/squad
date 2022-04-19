from typing import Optional

from sqlmodel import Field, SQLModel


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
