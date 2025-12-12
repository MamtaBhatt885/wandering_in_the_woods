# game/movement.py
import random

def random_move():
    moves = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]
    return random.choice(moves)
