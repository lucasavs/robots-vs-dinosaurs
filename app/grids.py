from fastapi import HTTPException

grid_number = 0
robot_counter = {}
GRID_SIZE = 50
robots_tracker = {}
grids = {}


def get_new_robot_id(grid_id):
    if not robot_counter.get(grid_id):
        robot_counter[grid_id] = 0
    old_robot_id = robot_counter[grid_id]
    robot_counter[grid_id] = robot_counter[grid_id] + 1
    return old_robot_id


def update_robot_tracker(grid_id, robot):
    if not robots_tracker.get(grid_id):
        robots_tracker[grid_id] = {}

    robots_tracker[grid_id][robot.id] = robot


def insert_element(grid_id, position_x, position_y, new_info):
    grid = grids.get(grid_id)
    if not grid:
        raise HTTPException(status_code=404, detail="grid not found")

    if grid[position_x][position_y] is not None:
        raise HTTPException(status_code=400, detail="space occupied")

    if position_x < 0 or position_x > 49 or position_y < 0 or position_y > 49:
        raise Exception("new position is invalid")

    grids[grid_id][position_x][position_y] = new_info


def delete_element(grid_id, position_x, position_y):
    grid = grids.get(grid_id)
    if not grid:
        raise HTTPException(status_code=404, detail="grid not found")

    if position_x < 0 or position_x > 49 or position_y < 0 or position_y > 49:
        raise Exception("new position is invalid")

    grids[grid_id][position_x][position_y] = None


def get_element(grid_id, position_x, position_y):
    grid = grids.get(grid_id)
    if not grid:
        raise HTTPException(status_code=404, detail="grid not found")

    return grids[grid_id][position_x][position_y]
