from fastapi.testclient import TestClient
from sqlmodel import Session

from jokes_api.models import Joke


def test_create_joke(client: TestClient):
    response = client.post(
        "/jokes/", json={"icon": "string", "joke": "string", "url": "string"}
    )
    data = response.json()
    assert response.status_code == 200
    assert data.get("id") == 1


def test_delete_joke(session: Session, client: TestClient):
    joke_1 = Joke(joke="Funny Joke")
    session.add(joke_1)
    session.commit()
    response = client.delete(f"/jokes/{joke_1.id}")
    joke_in_db = session.get(Joke, joke_1.id)
    assert response.status_code == 200
    assert joke_in_db is None


def test_delete_joke_fail_by_id(session: Session, client: TestClient):
    response = client.delete("/jokes/144564564")
    assert response.status_code == 404


def test_update_joke(session: Session, client: TestClient):
    joke = Joke(joke="Funny Joke")
    session.add(joke)
    session.commit()

    response = client.patch(
        f"/jokes/{joke.id}", json={"joke": "The funniest joke in the world"}
    )
    data = response.json()

    assert response.status_code == 200
    assert data["joke"] == "The funniest joke in the world"
    assert data["id"] == joke.id


def test_update_joke_fail_by_id(session: Session, client: TestClient):
    response = client.patch(
        "/jokes/144564564", json={"joke": "The funniest joke in the world"}
    )
    assert response.status_code == 404


def test_get_random_joke(client: TestClient):
    response = client.get("/random_jokes/")
    data = response.json()
    assert response.status_code == 200
    assert "Dad" or "Chuck" in data["type_joke"]


def test_get_random_dad_joke(client: TestClient):
    response = client.get("/random_jokes/", params={"type_joke": "Dad"})
    data = response.json()
    assert response.status_code == 200
    assert "Dad" in data["type_joke"]


def test_get_random_chuck_joke(client: TestClient):
    response = client.get("/random_jokes/", params={"type_joke": "Chuck"})
    data = response.json()
    assert response.status_code == 200
    assert "Chuck" in data["type_joke"]


def test_fail_get_random_joke_by_param(client: TestClient):
    response = client.get("/random_jokes/", params={"type_joke": "Fail"})
    assert response.status_code == 400


def test_read_jokes(session: Session, client: TestClient):
    joke_1 = Joke(joke="Funny Joke")
    session.add(joke_1)
    session.commit()

    response = client.get("/jokes/")
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0
