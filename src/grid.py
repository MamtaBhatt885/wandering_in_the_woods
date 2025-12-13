import pygame
from src.config import CELL_SIZE, GRID_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.width = cols * CELL_SIZE
        self.height = rows * CELL_SIZE

        self.offset_x = (SCREEN_WIDTH - self.width) // 2
        self.offset_y = (SCREEN_HEIGHT - self.height) // 2

    def draw(self, screen):
        for r in range(self.rows):
            for c in range(self.cols):
                rect = pygame.Rect(
                    self.offset_x + c * CELL_SIZE,
                    self.offset_y + r * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
                # ✅ ONLY border, no fill
                pygame.draw.rect(screen, GRID_COLOR, rect, 1)
