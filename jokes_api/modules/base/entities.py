from typing import Optional

from pydantic import BaseModel


class ResultJoke(BaseModel):
    icon: Optional[str]
    id_joke: str
    joke: str
    url: Optional[str]
