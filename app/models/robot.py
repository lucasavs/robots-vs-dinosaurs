from .fighter import Fighter
from ..grids import Grids


class Robot(Fighter):
    id = None

    def turn(self, direction):
        if direction == "left":
            if self.facing == "up":
                self.facing = "left"
            elif self.facing == "left":
                self.facing = "down"
            elif self.facing == "down":
                self.facing = "right"
            elif self.facing == "right":
                self.facing = "up"
        else:
            if self.facing == "up":
                self.facing = "right"
            elif self.facing == "left":
                self.facing = "up"
            elif self.facing == "down":
                self.facing = "right"
            elif self.facing == "right":
                self.facing = "down"

    def attack(self):
        if self.position_y - 1 >= 0:
            Grids.delete_element(self.grid_id, self.position_x, self.position_y - 1)
        if self.position_x - 1 >= 0:
            Grids.delete_element(self.grid_id, self.position_x - 1, self.position_y)
        if self.position_y + 1 <= 49:
            Grids.delete_element(self.grid_id, self.position_x, self.position_y + 1)
        if self.position_x + 1 <= 49:
            Grids.delete_element(self.grid_id, self.position_x + 1, self.position_y)

    def move(self, direction):
        new_x = self.position_x
        new_y = self.position_y
        if direction == "forward":
            if self.facing == "up":
                new_x = new_x - 1
            elif self.facing == "left":
                new_y = new_y - 1
            elif self.facing == "down":
                new_x = new_x + 1
            elif self.facing == "right":
                new_y = new_y + 1
        else:
            if self.facing == "up":
                new_x = new_x + 1
            elif self.facing == "left":
                new_y = new_y + 1
            elif self.facing == "down":
                new_x = new_x - 1
            elif self.facing == "right":
                new_y = new_y - 1

        Grids.insert_element(self.grid_id, new_x, new_y, self)
        Grids.delete_element(self.grid_id, self.position_x, self.position_y)
        self.position_x = new_x
        self.position_y = new_y

    def print(self):
        personification = "🤖"
        if self.facing == "up":
            personification += "⬆"
        elif self.facing == "left":
            personification += "⬅️"
        elif self.facing == "right":
            personification += "➡️"
        elif self.facing == "down":
            personification += "⬇️"
        return personification

    def create(self):
        super().create()
        self.id = Grids.get_new_robot_id(self.grid_id)
        Grids.update_robot_tracker(self.grid_id, self)
        return self.id
