from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)


def test_create_dinosaur():
    response = client.post("/grid/create/")

    assert response.status_code == 200

    body = json.loads(response.text)

    new_response = client.post(
        "/dinosaur/create/",
        json={
            "grid_id": body["grid_id"],
            "position_x": 2,
            "position_y": 2,
        },
    )
    assert new_response.status_code == 200


def test_create_dinosaur_in_same_space():
    response = client.post("/grid/create/")

    body = json.loads(response.text)

    client.post(
        "/dinosaur/create/",
        json={
            "grid_id": body["grid_id"],
            "position_x": 2,
            "position_y": 2,
        },
    )
    new_response = client.post(
        "/dinosaur/create/",
        json={
            "grid_id": body["grid_id"],
            "position_x": 2,
            "position_y": 2,
        },
    )
    new_body = json.loads(new_response.text)
    assert new_response.status_code == 400
    assert new_body["detail"] == "space occupied"
