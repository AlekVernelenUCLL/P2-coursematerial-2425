class CircularBuffer():
    def __init__(self, last_items):
        self.length = []

    def add(self, item):
        self.length.append(item)