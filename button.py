import pygame


class Button:

    def __init__(self, color, x, y, width, height, text):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def render(self, surface, outline=None):
        if outline:
            pygame.draw.rect(surface, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height), 0)
        font = pygame.font.SysFont('arial', 36)
        text = font.render(self.text, True, (0, 0, 0))
        surface.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_hovering(self, position):
        return self.x < position[0] < self.x + self.width and self.y < position[1] < self.y + self.height
