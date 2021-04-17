from fastapi.testclient import TestClient
from app.main import app
import json
from app.grids import Grids
import pytest

client = TestClient(app)


def test_not_retrieving_invalid_robot():
    Grids.reset()
    response = client.post("/grid/create/")
    assert response.status_code == 200

    body = json.loads(response.text)
    new_response = client.post(
        "/robot/instruction/",
        json={
            "grid_id": body["grid_id"],
            "robot_id": 0,
            "instruction": "move",
            "direction": "forward",
        },
    )
    assert new_response.status_code == 404


def test_create_robot():
    Grids.reset()
    response = client.post("/grid/create/")

    assert response.status_code == 200

    body = json.loads(response.text)

    new_response = client.post(
        "/robot/create/",
        json={
            "grid_id": body["grid_id"],
            "position_x": 2,
            "position_y": 2,
            "facing": "up",
        },
    )
    assert new_response.status_code == 200


def test_create_robot_in_same_space():
    Grids.reset()
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


def test_create_two_robots_same_position_different_grids():
    Grids.reset()

    response = client.post("/grid/create/")
    body = json.loads(response.text)
    first_grid_id = body["grid_id"]

    response = client.post("/grid/create/")
    body = json.loads(response.text)
    second_grid_id = body["grid_id"]

    first_response = client.post(
        "/robot/create/",
        json={
            "grid_id": first_grid_id,
            "position_x": 2,
            "position_y": 2,
            "facing": "up",
        },
    )

    second_response = client.post(
        "/robot/create/",
        json={
            "grid_id": second_grid_id,
            "position_x": 2,
            "position_y": 2,
            "facing": "up",
        },
    )

    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert first_grid_id != second_grid_id


def test_robot_cant_move_outside_grid():
    Grids.reset()

    grid = client.post("/grid/create/")
    body = json.loads(grid.text)
    grid_id = body["grid_id"]

    robot = client.post(
        "/robot/create/",
        json={
            "grid_id": grid_id,
            "position_x": 1,
            "position_y": 1,
            "facing": "left",
        },
    )
    body = json.loads(robot.text)
    robot_id = body["robot_id"]

    response = client.post(
        "/robot/instruction/",
        json={
            "grid_id": grid_id,
            "robot_id": robot_id,
            "instruction": "move",
            "direction": "forward",
        },
    )
    assert response.status_code == 200

    response = client.post(
        "/robot/instruction/",
        json={
            "grid_id": grid_id,
            "robot_id": robot_id,
            "instruction": "move",
            "direction": "forward",
        },
    )
    body = json.loads(response.text)
    assert response.status_code == 400
    assert body["detail"] == "new position is invalid"


def test_robot_kill_dinosaur_and_take_it_place():
    Grids.reset()
    grid = client.post("/grid/create/")
    body = json.loads(grid.text)
    grid_id = body["grid_id"]

    robot = client.post(
        "/robot/create/",
        json={
            "grid_id": grid_id,
            "position_x": 2,
            "position_y": 2,
            "facing": "up",
        },
    )
    body = json.loads(robot.text)
    robot_id = body["robot_id"]
    client.post(
        "/dinosaur/create/",
        json={
            "grid_id": grid_id,
            "position_x": 1,
            "position_y": 2,
        },
    )

    response = client.post(
        "/robot/instruction/",
        json={
            "grid_id": grid_id,
            "robot_id": robot_id,
            "instruction": "move",
            "direction": "forward",
        },
    )
    body = json.loads(response.text)
    assert response.status_code == 400
    assert body["detail"] == "space occupied"

    client.post(
        "/robot/instruction/",
        json={
            "grid_id": grid_id,
            "robot_id": robot_id,
            "instruction": "attack",
        },
    )

    response = client.post(
        "/robot/instruction/",
        json={
            "grid_id": grid_id,
            "robot_id": robot_id,
            "instruction": "move",
            "direction": "forward",
        },
    )
    body = json.loads(response.text)
    assert response.status_code == 200
