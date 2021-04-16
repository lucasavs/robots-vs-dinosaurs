from ..models.dinosaur import Dinosaur


def create(grid_id, position_x, position_y):
    dinosaur = Dinosaur(grid_id, position_x, position_y)
    dinosaur.create()
