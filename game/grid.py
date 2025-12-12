from config.settings import GRID_SIZE

def cell_to_pixels(row, col):
    x = col * GRID_SIZE
    y = row * GRID_SIZE
    return x, y
