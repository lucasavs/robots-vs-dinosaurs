from ..grids import grid_number, grids, GRID_SIZE
from fastapi import HTTPException

def create_grid():
    global grid_number
    global grids
    global GRID_SIZE
    grid = [ [ None for i in range(GRID_SIZE) ] for j in range(GRID_SIZE) ]
    grids[grid_number] = grid
    old_grid_number = grid_number
    grid_number = grid_number + 1
    return old_grid_number

def get_grid(grid_number):
    grid = grids.get(grid_number)
    if not grid:
        raise HTTPException(status_code=404, detail="grid not found")
    return grid