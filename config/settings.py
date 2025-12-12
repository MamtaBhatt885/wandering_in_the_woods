# config/settings.py

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 30

# Grid size (number of rows/cols)
GRID_ROWS = 12
GRID_COLS = 16

# Cell size is computed based on window
CELL_WIDTH = WINDOW_WIDTH // GRID_COLS
CELL_HEIGHT = WINDOW_HEIGHT // GRID_ROWS
