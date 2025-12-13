import random

class Player:
    def __init__(self, pid, row, col):
        self.id = pid
        self.row = row
        self.col = col
        self.moves = 0

    def move(self, rows, cols):
        direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

        if direction == "UP" and self.row > 0:
            self.row -= 1
        elif direction == "DOWN" and self.row < rows - 1:
            self.row += 1
        elif direction == "LEFT" and self.col > 0:
            self.col -= 1
        elif direction == "RIGHT" and self.col < cols - 1:
            self.col += 1

        self.moves += 1
