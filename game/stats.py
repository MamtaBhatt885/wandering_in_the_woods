# game/stats.py
import time

class Stats:
    def __init__(self):
        self.start_time = time.time()
        self.end_time = None

    def finish(self):
        self.end_time = time.time()

    def get_duration(self):
        if self.end_time is None:
            return 0
        return round(self.end_time - self.start_time, 2)
