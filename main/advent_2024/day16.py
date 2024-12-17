from _heapq import heappush, heappop
from math import inf

from main.utils.coord_utils import Coord
from main.utils.directions_utils import directions
from main.utils.files_utils import lire_fichier

orientations = ["N", "E", "S", "O"]


class Path:

    def __init__(self, last: Coord,
                 # path: set[Coord],
                 orientation: str, score: int):
        self.last = last
        # self.path = path
        self.orientation = orientation
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

def part1(input_path):
    lignes = lire_fichier(input_path)
    walls: set[Coord] = set()
    start = None
    end = None
    for y, ligne in enumerate(lignes):
        if ligne == "":
            break
        for x, char in enumerate(ligne):
            if char == "#":
                walls.add(Coord(x, y))
            elif char == "S":
                start = Coord(x, y)
            elif char == "E":
                end = Coord(x, y)
    paths = []
    visited = set()
    heappush(paths, Path(start,
                         # {start},
                         "E", 0))
    min_score = inf
    while len(paths) > 0:
        path = heappop(paths)
        check = path.last
        if check in visited:
            continue
        visited.add(check)
        if check == end:
            if path.score < min_score:
                min_score = path.score
            continue
        for direction in orientations:
            new_case = check + directions[direction]
            # if wall do nothing
            # if already in path do nothing
            if new_case not in walls and new_case not in visited:
                turn_cost = 1000 if not direction == path.orientation else 0
                new_score = path.score + turn_cost + 1
                heappush(paths,
                         Path(new_case,
                              # path.path | {new_case},
                              direction, new_score))
    return min_score


class CoordOriente:
    def __init__(self, coord: Coord, direction: str):
        self.coord = coord
        self.direction = direction

    def __eq__(self, other):
        return self.coord == other.coord and self.direction == other.direction

    def __hash__(self):
        return hash((self.coord, self.direction))


class PathBis:

    def __init__(self, last: CoordOriente,
                 path: set[Coord], score: int):
        self.last = last
        self.path = path
        self.score = score

    def __lt__(self, other):
        return self.score < other.score


def part2(input_path):
    lignes = lire_fichier(input_path)
    walls: set[Coord] = set()
    start = None
    end = None
    for y, ligne in enumerate(lignes):
        if ligne == "":
            break
        for x, char in enumerate(ligne):
            if char == "#":
                walls.add(Coord(x, y))
            elif char == "S":
                start = Coord(x, y)
            elif char == "E":
                end = Coord(x, y)
    paths: list[PathBis] = []
    visited: dict[CoordOriente, int] = {}
    heappush(paths, PathBis(CoordOriente(start, "E"),
                            {start}, 0))
    min_score = inf
    coords_ok: set[Coord] = set()
    while len(paths) > 0:
        path = heappop(paths)
        check = path.last
        if check in visited.keys() and path.score > visited[check]:
            continue
        visited[check] = path.score
        if check.coord == end:
            if path.score <= min_score:
                min_score = path.score
                coords_ok.update(path.path)
            continue
        for direction in orientations:
            new_case = check.coord + directions[direction]
            # if wall do nothing
            # if already in path do nothing
            if new_case not in walls:
                turn_cost = 1000 if not direction == path.last.direction else 0
                new_score = path.score + turn_cost + 1
                heappush(paths,
                         PathBis(CoordOriente(new_case, direction),
                                 path.path | {new_case},
                                 new_score))
    draw_grid(walls, coords_ok, len(lignes[0]), len(lignes))
    return len(coords_ok)


def draw_grid(walls, coords_ok, max_x, max_y):
    out = ""
    for y in range(max_y):
        for x in range(max_x):
            if Coord(x, y) in walls:
                out += "#"
            elif Coord(x, y) in coords_ok:
                out += "O"
            else:
                out += "."
        out += "\n"
    print(out)
