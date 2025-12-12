import pygame
import random
from config.settings import ROWS, COLS, GRID_SIZE
from game.grid import cell_to_pixels

class Character:
    def __init__(self, sprite_path, start_pos):
        self.sprite = pygame.transform.scale(
            pygame.image.load(sprite_path),
            (40, 40)
        )
        self.row, self.col = start_pos
        self.steps = 0

    def draw(self, window):
        x, y = cell_to_pixels(self.row, self.col)
        window.blit(self.sprite, (x + 5, y + 5))

    def random_move(self):
        direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

        if direction == "UP" and self.row > 0:
            self.row -= 1
        elif direction == "DOWN" and self.row < ROWS - 1:
            self.row += 1
        elif direction == "LEFT" and self.col > 0:
            self.col -= 1
        elif direction == "RIGHT" and self.col < COLS - 1:
            self.col += 1

        self.steps += 1
