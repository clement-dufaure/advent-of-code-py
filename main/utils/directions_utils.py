from main.utils.coord_utils import Coord

directions = {
    "N": Coord(0, -1),
    "NE": Coord(1, -1),
    "E": Coord(1, 0),
    "SE": Coord(1, 1),
    "S": Coord(0, 1),
    "SO": Coord(-1, 1),
    "O": Coord(-1, 0),
    "NO": Coord(-1, -1)
}
