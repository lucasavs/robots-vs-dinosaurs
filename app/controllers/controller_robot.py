from ..models.robot import Robot


def create_robot(grid, position_x, position_y, facing):
    robot = Robot(grid, position_x, position_y, facing)
    robot.create()
