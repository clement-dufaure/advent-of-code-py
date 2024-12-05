class Coord:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __mul__(self, autre):
        if isinstance(autre, int):
            return Coord(self.x * autre, self.y * autre)
        raise TypeError(f"Multiplication non supportée entre 'Coord' et {type(autre)}")

    def __rmul__(self, autre):
        return self.__mul__(autre)

    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"({self.x},{self.y})"
