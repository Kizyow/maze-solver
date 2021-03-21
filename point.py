class Point:
    wall_pairs = {'N': 'S',
                  'S': 'N',
                  'E': 'W',
                  'W': 'E'}

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.data = None

        self.walls = {'N': True,
                      'E': True,
                      'S': True,
                      'W': True}

    def __str__(self):
        return str(self.x) + ', ' + str(self.y) + ', ' + str(self.walls)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def define_start_point(self):
        self.data = 'START'

    def define_exit_point(self):
        self.data = 'EXIT'

    def is_start_point(self):
        return self.data == 'START'

    def is_exit_point(self):
        return self.data == 'EXIT'

    def have_wall(self, key):
        return self.walls[key]

    def have_all_walls(self):
        return all(self.walls.values())

    def break_wall(self, other_point, direction):
        self.walls[direction] = False
        opposed_direction = self.wall_pairs[direction]
        other_point.walls[opposed_direction] = False
