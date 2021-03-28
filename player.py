# Une classe permettant de représenter un acteur dans le labyrinthe

class Player:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

    def up(self):
        self.y -= 1

    def down(self):
        self.y += 1
