from .fighter import Fighter


class Robot(Fighter):
    # facing = None
    # def __init__(self, facing):
    #     self.facing = facing

    def turn(self, direction):
        raise NotImplemented

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
