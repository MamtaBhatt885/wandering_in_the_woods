def collided(c1, c2):
    return c1.row == c2.row and c1.col == c2.col

def reset_positions(c1, c2):
    c1.row, c1.col = 0, 0
    c2.row, c2.col = 9, 11
    c1.steps = 0
    c2.steps = 0
