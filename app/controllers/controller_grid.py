from ..grids import Grids
from fastapi import HTTPException


def create_grid():
    grid_id = Grids.create_grid()
    return grid_id


def get_grid(grid_number):
    grid = Grids.grids.get(grid_number)
    if not grid:
        raise HTTPException(status_code=404, detail="grid not found")
    grid_draw = ""
    position_x = 0
    for line in grid:
        position_y = 0
        for element in line:
            if not element:
                grid_draw += str(position_x) + "-" + str(position_y)
            else:
                grid_draw += element.print()
            grid_draw += " "
            position_y = position_y + 1
        grid_draw += " "
        position_x = position_x + 1
    return grid_draw


def draw_grid(grid_number):
    grid = Grids.grids.get(grid_number)
    drawed_grid = []
    if not grid:
        raise HTTPException(status_code=404, detail="grid not found")
    position_x = 0
    for line in grid:
        position_y = 0
        new_line = []
        for element in line:
            if not element:
                new_line.append(str(position_x) + "-" + str(position_y))
            else:
                new_line.append(element.print())
            position_y = position_y + 1
        drawed_grid.append(new_line)
        position_x = position_x + 1
    return drawed_grid
