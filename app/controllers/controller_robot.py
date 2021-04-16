from ..models.robot import Robot
from ..grids import robots_tracker
from fastapi import HTTPException


def create_robot(grid_id, position_x, position_y, facing):
    robot = Robot(grid_id, position_x, position_y, facing)
    robot.create()
    return robot.id


def turn_robot(grid_id, robot_id, direction):
    robot = get_robot(grid_id, robot_id)
    robot.turn(direction)


def get_robot(grid_id, robot_id):
    if not robots_tracker.get(grid_id):
        raise HTTPException(status_code=404, detail="grid not found")
    if not robots_tracker[grid_id].get(robot_id):
        raise HTTPException(status_code=404, detail="robot")
    return robots_tracker[grid_id][robot_id]
