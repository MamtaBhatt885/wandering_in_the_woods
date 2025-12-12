import pygame

class Button:
    def __init__(self, text, pos, size=(200, 50)):
        self.font = pygame.font.SysFont("Arial", 32)
        self.text = text
        self.x, self.y = pos
        self.width, self.height = size
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        pygame.draw.rect(window, (200, 200, 200), self.rect)
        label = self.font.render(self.text, True, (0, 0, 0))
        window.blit(label, (self.x + 10, self.y + 10))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)
