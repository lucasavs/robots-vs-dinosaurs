from .fighter import Fighter
from ..grids import get_new_robot_id, update_robot_tracker


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
        raise NotImplemented

    def move(self, direction):
        raise NotImplemented

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
        self.id = get_new_robot_id(self.grid_id)
        update_robot_tracker(self.grid_id, self)
        return self.id
