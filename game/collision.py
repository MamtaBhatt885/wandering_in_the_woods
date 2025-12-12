# game/collision.py

def collided(c1, c2):
    return c1.row == c2.row and c1.col == c2.col
