from app.grids import Grids
from unittest.mock import MagicMock
import pytest
from fastapi import HTTPException


def test_get_new_robot_id():
    Grids.reset()
    robot_id = Grids.get_new_robot_id(0)

    assert Grids.robot_counter[0] == 1
    assert robot_id == 0


def test_update_robot_tracker():
    Grids.reset()

    robot = MagicMock()
    robot.id.return_value = 1

    Grids.update_robot_tracker(0, robot)

    assert Grids.robots_tracker == {0: {robot.id: robot}}


def test_insert_element_grid_not_foud():
    Grids.reset()
    element = MagicMock()
    with pytest.raises(HTTPException) as e:
        Grids.insert_element(0, 1, 2, element)
    assert e.value.status_code == 404
    assert e.value.detail == "grid not found"


def test_insert_element_space_occupied():
    Grids.reset()
    grid_id = Grids.create_grid()
    element = MagicMock()
    Grids.insert_element(grid_id, 1, 2, element)
    with pytest.raises(HTTPException) as e:
        Grids.insert_element(grid_id, 1, 2, element)
    assert e.value.status_code == 400
    assert e.value.detail == "space occupied"


def test_insert_element_invalid_position():
    Grids.reset()
    grid_id = Grids.create_grid()
    element = MagicMock()
    with pytest.raises(HTTPException) as e:
        Grids.insert_element(grid_id, -1, 10, element)
    assert e.value.status_code == 400
    assert e.value.detail == "new position is invalid"

    with pytest.raises(HTTPException) as e:
        Grids.insert_element(grid_id, 50, 10, element)
    assert e.value.status_code == 400
    assert e.value.detail == "new position is invalid"

    with pytest.raises(HTTPException) as e:
        Grids.insert_element(grid_id, 10, -1, element)
    assert e.value.status_code == 400
    assert e.value.detail == "new position is invalid"

    with pytest.raises(HTTPException) as e:
        Grids.insert_element(grid_id, 10, 50, element)
    assert e.value.status_code == 400
    assert e.value.detail == "new position is invalid"


def test_insert_element():
    Grids.reset()
    grid_id = Grids.create_grid()
    element = MagicMock()
    Grids.insert_element(grid_id, 10, 10, element)
    assert Grids.grids[grid_id][10][10] == element


def test_delete_element_grid_not_found():
    Grids.reset()
    with pytest.raises(HTTPException) as e:
        Grids.delete_element(0, 1, 2)
    assert e.value.status_code == 404
    assert e.value.detail == "grid not found"


def test_delete_element_invalid_position():
    Grids.reset()
    grid_id = Grids.create_grid()
    with pytest.raises(HTTPException) as e:
        Grids.delete_element(grid_id, -1, 10)
    assert e.value.status_code == 400
    assert e.value.detail == "position is invalid"

    with pytest.raises(HTTPException) as e:
        Grids.delete_element(grid_id, 50, 10)
    assert e.value.status_code == 400
    assert e.value.detail == "position is invalid"

    with pytest.raises(HTTPException) as e:
        Grids.delete_element(grid_id, 10, -1)
    assert e.value.status_code == 400
    assert e.value.detail == "position is invalid"

    with pytest.raises(HTTPException) as e:
        Grids.delete_element(grid_id, 10, 50)
    assert e.value.status_code == 400
    assert e.value.detail == "position is invalid"


def test_delete_element():
    Grids.reset()
    grid_id = Grids.create_grid()
    element = MagicMock()
    Grids.insert_element(grid_id, 10, 10, element)
    assert Grids.grids[grid_id][10][10] == element

    Grids.delete_element(grid_id, 10, 10)
    assert Grids.grids[grid_id][10][10] is None


def test_get_element_grid_not_found():
    Grids.reset()
    with pytest.raises(HTTPException) as e:
        Grids.get_element(0, 1, 2)
    assert e.value.status_code == 404
    assert e.value.detail == "grid not found"


def test_get_element():
    Grids.reset()
    grid_id = Grids.create_grid()
    element = MagicMock()
    Grids.insert_element(grid_id, 10, 10, element)
    assert Grids.grids[grid_id][10][10] == element

    new_element = Grids.get_element(grid_id, 10, 10)
    assert new_element == element


def test_create_grid():
    Grids.reset()
    grid_id = Grids.create_grid()

    assert len(Grids.grids[grid_id]) == 50
