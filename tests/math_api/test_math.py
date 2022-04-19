from fastapi.testclient import TestClient


def test_get_least_common_multiple(client: TestClient):
    response = client.get("/least_common_multiple/?numbers=50&numbers=15&numbers=5")
    data = response.json()
    assert response.status_code == 200
    assert data["least_common_multiple"] == 150


def test_get_least_common_multiple_fail(client: TestClient):
    response = client.get("/least_common_multiple/")
    assert response.status_code == 400


def test_get_number_plus_one(client: TestClient):
    response = client.get("/plus_one/?number=3")
    data = response.json()
    assert response.status_code == 200
    assert data["number_plus_one"] == 4


def test_get_number_plus_one_fail(client: TestClient):
    response = client.get("/plus_one/")
    assert response.status_code == 400
