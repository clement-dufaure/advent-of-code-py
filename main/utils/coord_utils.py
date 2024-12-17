class Coord:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, int):
            # multiplication par un scalaire
            return Coord(self.x * other, self.y * other)
        if isinstance(other, Coord):
            # produit scalaire
            return self.x * other.x + self.y * other.y
        raise TypeError(f"mul not supported between 'Coord' and {type(other)}")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other):
        if isinstance(other, Coord):
            if not self.y == other.y:
                return self.y < other.y
            else:
                return self.x < other.x
        raise TypeError(f"lt not supported between 'Coord' and {type(other)}")

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"({self.x},{self.y})"
