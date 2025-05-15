class Memory:
    def __init__(self):
        self.memory = 0.0

    def add(self, val):
        self.memory += val

    def subtract(self, val):
        self.memory -= val

    def recall(self):
        return self.memory

    def clear(self):
        self.memory = "No History"