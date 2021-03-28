from point import Point
import random


# Une classe permettant de générer un labyrinthe de taille définie et de le résoudre

class Maze:
    directions = [('W', (-1, 0)),
                  ('E', (1, 0)),
                  ('S', (0, 1)),
                  ('N', (0, -1))]

    def __init__(self, rows, columns, start_x=0, start_y=0):
        self.rows = rows
        self.columns = columns
        self.start_x = start_x
        self.start_y = start_y
        self.grid = [[Point(x, y) for y in range(self.columns)] for x in range(self.rows)]
        self.solution = []

    def get_point(self, x, y):
        return self.grid[x][y]

    def get_grid(self):
        return self.grid

    def get_solution(self):
        return self.solution

    def find_generation_neighbours(self, point):
        neighbours = []

        for direction, (direction_x, direction_y) in self.directions:
            next_x, next_y = point.get_x() + direction_x, point.get_y() + direction_y

            if (0 <= next_x < self.rows) and (0 <= next_y < self.columns):
                next_point = self.get_point(next_x, next_y)
                if next_point.have_all_walls():
                    neighbour = (direction, next_point)
                    neighbours.append(neighbour)

        return neighbours

    def generate_maze(self):

        maze_size = self.rows * self.columns
        current_size = 1
        pile = []
        current_point = self.get_point(self.start_x, self.start_y)

        while current_size < maze_size:
            neighbours = self.find_generation_neighbours(current_point)

            if not neighbours:
                current_point = pile.pop()
                continue

            direction, next_point = random.choice(neighbours)
            current_point.break_wall(next_point, direction)
            pile.append(current_point)
            current_point = next_point
            current_size += 1

        self.grid[self.start_x][self.start_y].define_start_point()
        self.grid[-1][-1].define_exit_point()

    def find_solve_neighbours(self, point, have_visited):
        neighbours = []

        for direction, (direction_x, direction_y) in self.directions:
            next_x, next_y = point.get_x() + direction_x, point.get_y() + direction_y

            if (0 <= next_x < self.rows) and (0 <= next_y < self.columns):
                next_point = self.get_point(next_x, next_y)

                if next_point in have_visited:
                    continue

                opposed_direction = Point.wall_pairs[direction]
                if not next_point.have_wall(opposed_direction):
                    neighbours.append(next_point)

        return neighbours

    def solve_maze(self):

        pile = []
        have_visited = []
        found_exit = False
        current_point = self.get_point(self.start_x, self.start_y)

        if current_point.have_all_walls():
            return

        while not found_exit:
            neighbours = self.find_solve_neighbours(current_point, have_visited)
            have_visited.append(current_point)

            if current_point.is_exit_point():
                found_exit = True
                continue

            if not neighbours:
                current_point = pile.pop()
                continue

            next_point = random.choice(neighbours)
            pile.append(current_point)
            current_point = next_point

        self.solution = pile
