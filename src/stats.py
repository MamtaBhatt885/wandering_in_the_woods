class Stats:
    def __init__(self):
        self.runs = []

    def add_run(self, moves):
        self.runs.append(moves)

    def summary(self):
        if not self.runs:
            return 0, 0, 0
        return min(self.runs), max(self.runs), sum(self.runs) / len(self.runs)
