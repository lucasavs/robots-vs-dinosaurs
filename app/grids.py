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
