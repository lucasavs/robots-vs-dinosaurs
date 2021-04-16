from ..grids import insert_element
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
        insert_element(self.grid_id, self.position_x, self.position_y, self)

    def print(self):
        raise NotImplementedError
