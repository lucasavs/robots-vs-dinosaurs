from fastapi import HTTPException


class Grids:

    grid_number = 0
    robot_counter = {}
    GRID_SIZE = 50
    robots_tracker = {}
    grids = {}

    @classmethod
    def get_new_robot_id(cls, grid_id):
        if not cls.robot_counter.get(grid_id):
            cls.robot_counter[grid_id] = 0
        old_robot_id = cls.robot_counter[grid_id]
        cls.robot_counter[grid_id] = cls.robot_counter[grid_id] + 1
        return old_robot_id

    @classmethod
    def update_robot_tracker(cls, grid_id, robot):
        if not cls.robots_tracker.get(grid_id):
            cls.robots_tracker[grid_id] = {}

        cls.robots_tracker[grid_id][robot.id] = robot

    @classmethod
    def insert_element(cls, grid_id, position_x, position_y, new_info):
        grid = cls.grids.get(grid_id)
        if not grid:
            raise HTTPException(status_code=404, detail="grid not found")

        if grid[position_x][position_y] is not None:
            raise HTTPException(status_code=400, detail="space occupied")

        if position_x < 0 or position_x > 49 or position_y < 0 or position_y > 49:
            raise HTTPException(status_code=400, detail="new position is invalid")

        cls.grids[grid_id][position_x][position_y] = new_info

    @classmethod
    def delete_element(cls, grid_id, position_x, position_y):
        grid = cls.grids.get(grid_id)
        if not grid:
            raise HTTPException(status_code=404, detail="grid not found")

        if position_x < 0 or position_x > 49 or position_y < 0 or position_y > 49:
            raise HTTPException(status_code=400, detail="new position is invalid")

        cls.grids[grid_id][position_x][position_y] = None

    @classmethod
    def get_element(cls, grid_id, position_x, position_y):
        grid = cls.grids.get(grid_id)
        if not grid:
            raise HTTPException(status_code=404, detail="grid not found")

        return cls.grids[grid_id][position_x][position_y]
