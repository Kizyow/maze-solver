import pygame
from color import *
from maze import Maze
from button import Button
from textbox import TextBox
from player import Player


# Une classe permettant de représenter graphiquement le labyrinthe et de pouvoir le configurer et de faire évoluer un
# acteur

class Interface:

    # Initialisation de l'interface graphique
    def __init__(self, name, width, height):
        self.width = width
        self.height = height
        screen_size = (width, height)

        pygame.init()
        pygame.display.set_caption(name)

        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.running = False

        self.row = 10
        self.column = 10
        self.pad = 100
        self.maze_screen = 500

        self.cell_size = min(self.maze_screen / self.row, self.maze_screen / self.column)
        self.maze = Maze(self.row, self.column)

        self.text_box = TextBox(675, 150, 250, 100, '10x10')
        self.generate_button = Button(gray, 675, 300, 250, 100, "Generate")
        self.solve_button = Button(gray, 675, 450, 250, 100, "Solve")

        self.player = Player(0, 0)

    # Permet de faire démarrer le programme et de faire exécuter le code a chaque frame (évenements, graphisme...)
    def start(self):
        self.running = True

        while self.running:
            self.clock.tick(30)
            self.event()
            self.render()

    # Permet de quitter le programme
    def stop(self):
        self.running = False
        pygame.quit()

    # Met à jour la taille du labyrinthe par rapport à l'input de l'utilisateur
    def update_maze(self):
        text = self.text_box.text
        x, y = text.split('x')
        self.row = int(x)
        self.column = int(y)

    # Un écouteur d'évenements (listener) pour exécuter des actions spécifiques
    def event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    if self.generate_button.is_hovering(pygame.mouse.get_pos()):
                        self.update_maze()
                        self.cell_size = min(self.maze_screen / self.row, self.maze_screen / self.column)
                        self.maze = Maze(self.row, self.column)

                        self.maze.generate_maze()
                        self.player = Player()

                    if self.solve_button.is_hovering(pygame.mouse.get_pos()):
                        self.maze.solve_maze()

            if event.type == pygame.KEYDOWN:

                point = self.maze.get_point(self.player.get_x(), self.player.get_y())

                if event.key == pygame.K_DOWN and not point.have_wall('S'):
                    self.player.down()
                if event.key == pygame.K_UP and not point.have_wall('N'):
                    self.player.up()
                if event.key == pygame.K_LEFT and not point.have_wall('W'):
                    self.player.left()
                if event.key == pygame.K_RIGHT and not point.have_wall('E'):
                    self.player.right()

                if event.key == pygame.K_BACKSPACE:
                    self.text_box.text = self.text_box.text[:-1]
                else:
                    self.text_box.text += event.unicode

    # Permet de rendre le programme graphiquement en général
    def render(self):
        if self.running:
            self.screen.fill(white)
            self.render_button()
            self.render_text_box()
            self.render_maze()

            pygame.draw.circle(self.screen, green, (
                self.cell_size * self.player.get_x() + self.pad + self.cell_size / 2,
                self.cell_size * self.player.get_y() + self.pad + self.cell_size / 2), 8)

            pygame.display.flip()

    # Permet de rendre graphiquement le labyrinthe uniquement
    def render_maze(self):
        for point in self.maze.get_solution():
            pygame.draw.circle(self.screen, blue, (
                self.cell_size * point.get_x() + self.pad + self.cell_size / 2,
                self.cell_size * point.get_y() + self.pad + self.cell_size / 2), 8)

        rows_size = len(self.maze.get_grid())
        for rows in range(rows_size):
            for point in self.maze.get_grid()[rows]:
                start_x, start_y = point.get_x() * self.cell_size + self.pad, point.get_y() * self.cell_size + self.pad
                end_x, end_y = (point.get_x() + 1) * self.cell_size + self.pad, (
                        point.get_y() + 1) * self.cell_size + self.pad

                if point.have_wall('S'):
                    self.draw_wall(start_x, end_y, end_x, end_y)

                if point.have_wall('E'):
                    self.draw_wall(end_x, start_y, end_x, end_y)

                if point.is_start_point():
                    pygame.draw.circle(self.screen, green, (
                        self.cell_size * point.get_x() + self.pad + self.cell_size / 2,
                        self.cell_size * point.get_y() + self.pad + self.cell_size / 2),
                                       10)

                if point.is_exit_point():
                    pygame.draw.circle(self.screen, red, (
                        self.cell_size * point.get_x() + self.pad + self.cell_size / 2,
                        self.cell_size * point.get_y() + self.pad + self.cell_size / 2),
                                       10)

        self.draw_wall(self.pad, self.pad, self.cell_size * self.row + self.pad, self.pad)
        self.draw_wall(self.pad, self.pad, self.pad, self.cell_size * self.column + self.pad)

    # Permet de rendre les boutons uniquement
    def render_button(self):
        self.generate_button.render(self.screen, (0, 0, 0))
        self.solve_button.render(self.screen, (0, 0, 0))

        mouse_pos = pygame.mouse.get_pos()
        if self.generate_button.is_hovering(mouse_pos):
            self.generate_button.color = light_blue
        else:
            self.generate_button.color = gray

        if self.solve_button.is_hovering(mouse_pos):
            self.solve_button.color = light_blue
        else:
            self.solve_button.color = gray

    # Permet de rendre l'entrée de texte uniquement
    def render_text_box(self):
        self.text_box.render(self.screen)

    # Permet de dessiner un mur pour plus de simplicité lors de la génération du labyrinthe
    def draw_wall(self, start_x, start_y, end_x, end_y, thickness=5):
        start_point = (start_x, start_y)
        end_point = (end_x, end_y)
        pygame.draw.line(self.screen, black, start_point, end_point, thickness)
