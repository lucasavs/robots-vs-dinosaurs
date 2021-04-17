from fastapi.testclient import TestClient
from app.main import app
import json
from app.grids import reset_grids
import pytest

client = TestClient(app)


def test_create_dinosaur():
    reset_grids()
    response = client.post("/grid/create/")

    assert response.status_code == 200

    body = json.loads(response.text)

    new_response = client.post(
        "/robot/create/",
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
        "/robot/create/",
        json={
            "grid_id": body["grid_id"],
            "position_x": 2,
            "position_y": 2,
            "facing": "up",
        },
    )
    new_response = client.post(
        "/robot/create/",
        json={
            "grid_id": body["grid_id"],
            "position_x": 2,
            "position_y": 2,
            "facing": "up",
        },
    )
    new_body = json.loads(new_response.text)
    assert new_response.status_code == 400
    assert new_body["detail"] == "space occupied"
