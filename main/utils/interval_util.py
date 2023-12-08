class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"({self.start}, {self.end})"

    def length(self):
        return self.end - self.start
