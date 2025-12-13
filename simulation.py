import pygame
from player import Player

class Simulation:
    def __init__(self, rows, cols, players, sound):
        self.rows = rows
        self.cols = cols
        self.players = players
        self.sound = sound
        self.finished = False

    def step(self):
        if self.finished:
            return

        for p in self.players:
            p.move(self.rows, self.cols)

        self.check_meetings()

    def check_meetings(self):
        positions = {}
        for p in self.players:
            pos = (p.row, p.col)
            positions.setdefault(pos, []).append(p)

        for same_cell in positions.values():
            if len(same_cell) > 1:
                self.sound.play()
                leader = same_cell[0]
                for p in same_cell[1:]:
                    self.players.remove(p)
                if len(self.players) == 1:
                    self.finished = True
