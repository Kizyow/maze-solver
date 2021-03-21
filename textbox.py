import pygame


class TextBox:

    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def render(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.width, self.height), 0)
        font = pygame.font.SysFont('arial', 36)
        text = font.render(self.text, True, (0, 0, 0))
        surface.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
