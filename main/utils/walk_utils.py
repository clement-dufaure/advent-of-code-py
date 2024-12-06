from main.utils.coord_utils import Coord


class Walk:

    def __init__(self, coord: Coord, direction: str):
        self.coord = coord
        self.direction = direction

    def __eq__(self, other):
        if isinstance(other, Walk):
            return self.coord == other.coord and self.direction == other.direction
        return False

    def __hash__(self):
        return hash((self.coord, self.direction))

    def __repr__(self):
        return f"{self.coord}->{self.direction}"
