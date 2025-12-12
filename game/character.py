# game/character.py
import pygame
from config.settings import CELL_WIDTH, CELL_HEIGHT

class Character:
    def __init__(self, sprite_path, start_pos):
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (CELL_WIDTH, CELL_HEIGHT))

        self.row, self.col = start_pos
        self.steps = 0

    def move(self, d_row, d_col, grid_rows, grid_cols):
        new_row = self.row + d_row
        new_col = self.col + d_col

        if 0 <= new_row < grid_rows and 0 <= new_col < grid_cols:
            self.row = new_row
            self.col = new_col
            self.steps += 1

    def draw(self, screen):
        x = self.col * CELL_WIDTH
        y = self.row * CELL_HEIGHT
        screen.blit(self.image, (x, y))
