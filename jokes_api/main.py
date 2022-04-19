import math
import random
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Session, select

from jokes_api.create_db import create_db_and_tables
from jokes_api.database import get_session
from jokes_api.models import Joke, JokeCreate, JokeRead, JokeUpdate
from jokes_api.modules.base.entities import ResultJoke
from jokes_api.modules.base.factory import jokes_factory

app = FastAPI()


@app.on_event("startup")
def on_startup():  # pragma: no cover
    create_db_and_tables()


@app.post("/jokes/", response_model=JokeRead, tags=["jokes"])
def joke(*, session: Session = Depends(get_session), joke: JokeCreate):
    """
    Add joke to own database
    - **joke**: Funny joke text
    - **icon**: Funny joke url image
    - **joke**: Funny joke url
    """
    db_joke = Joke.from_orm(joke)
    session.add(db_joke)
    session.commit()
    session.refresh(db_joke)
    return db_joke


@app.get("/jokes/", response_model=List[JokeRead], tags=["jokes"])
def read_jokes(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    """
    Get all Jokes from own database
    """
    jokes = session.exec(select(Joke).offset(offset).limit(limit)).all()
    return jokes


@app.patch("/jokes/{joke_id}", response_model=JokeRead, tags=["jokes"])
def update_joke(
    *, session: Session = Depends(get_session), joke_id: int, joke: JokeUpdate
):
    """
    Update joke from own database
    - **joke**: New joke text
    """
    db_joke = session.get(Joke, joke_id)
    if not db_joke:
        raise HTTPException(status_code=404, detail="Joke not found")
    hero_data = joke.dict(exclude_unset=True)
    for key, value in hero_data.items():
        setattr(db_joke, key, value)
    session.add(db_joke)
    session.commit()
    session.refresh(db_joke)
    return db_joke


@app.delete("/jokes/{joke_id}", tags=["jokes"])
def delete_joke(*, session: Session = Depends(get_session), joke_id: int):
    """
    Delete joke
    -**joke_id**: id to delete
    """
    joke = session.get(Joke, joke_id)
    if not joke:
        raise HTTPException(status_code=404, detail="Joke not found")
    session.delete(joke)
    session.commit()
    return {"ok": True}


@app.get("/random_jokes/", response_model=ResultJoke, tags=["random jokes"])
def random_joke(type_joke: Optional[str] = None):
    """Get a random joke from **https://api.chucknorris.io/**
     or  **https://icanhazdadjoke.com/api**
    - **type_joke**: query param options are (Chuck, Dad)

    """
    if type_joke is None:
        type_joke_random = random.choice(["Dad", "Chuck"])
        type_joke = type_joke_random
    type_joke = type_joke.capitalize()
    try:
        jokes = jokes_factory(type_joke)
        joke_content = jokes.get_random_joke()
        return joke_content
    except TypeError:
        raise HTTPException(status_code=400, detail="Options are only Dad and Chuck")


@app.get("/least_common_multiple/", tags=["math"])
def get_least_common_multiple(numbers: List[int] = Query(None)):
    """
    Get least common multiple from list of numbers
    **numbers**: Numbers to get lcm
    """
    if not numbers:
        raise HTTPException(status_code=400, detail="At least send one integer")
    least_common_multiple = math.lcm(*numbers)
    return {"least_common_multiple": least_common_multiple}


@app.get("/plus_one/", tags=["math"])
def get_number_plus_one(number: int = None):
    """
    Get numbers plus one
    """
    if not number:
        raise HTTPException(status_code=400, detail="At least send one integer")
    number += 1
    return {"number_plus_one": number}
