from ..grids import grids
from fastapi import HTTPException
from abc import ABC


class Fighter(ABC):
    grid_id = None
    position_x = None
    position_y = None
    facing = None

    def __init__(self, grid_id, position_x, position_y, facing=None):
        self.grid_id = grid_id
        self.position_x = position_x
        self.position_y = position_y
        self.facing = facing

    def create(self):
        grid = grids.get(self.grid_id)
        if not grid:
            raise HTTPException(status_code=404, detail="grid not found")

        if grid[self.position_x][self.position_y] is not None:
            raise HTTPException(status_code=400, detail="space occupied")

        grid[self.position_x][self.position_y] = self

    def print(self):
        raise NotImplementedError
