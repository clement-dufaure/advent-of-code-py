from heapq import heappush, heappop
from math import inf

from main.utils.coord_utils import Coord
from main.utils.directions_utils import directions
from main.utils.files_utils import lire_fichier


class Path:

    def __init__(self, last: Coord,
                 # path: set[Coord],
                 score: int):
        self.last = last
        # self.path = path
        self.score = score

    def __lt__(self, other):
        return self.score < other.score


orientations = ["N", "E", "S", "O"]


def part1(input_path, max_x=70, max_y=70, how_many_lines=1024):
    lignes = lire_fichier(input_path)
    bugs: set[Coord] = set()
    for ligne in lignes[:how_many_lines]:
        digits = list(map(int, ligne.split(",")))
        bugs.add(Coord(digits[0], digits[1]))
    paths: list[Path] = []
    visited = set()
    start = Coord(0, 0)
    end = Coord(max_x, max_y)
    heappush(paths, Path(start,
                         # {start},
                         0))
    while len(paths) > 0:
        path = heappop(paths)
        check = path.last
        if check in visited:
            continue
        visited.add(check)
        if check == end:
            return path.score
        for direction in orientations:
            new_case = check + directions[direction]
            # if bug do nothing or out of bounds
            # if already in path do nothing
            if (new_case not in bugs and 0 <= new_case.x <= max_x
                    and 0 <= new_case.y <= max_y and new_case not in visited):
                new_score = path.score + 1
                heappush(paths,
                         Path(new_case,
                              # path.path | {new_case},
                              new_score))
    return inf


def part2(input_path, max_x=70, max_y=70, start_i=1025):
    i = start_i
    lignes = lire_fichier(input_path)
    while True:
        print(f"Trying {i}")
        out = part1(input_path, max_x=max_x, max_y=max_y, how_many_lines=i)
        if out == inf:
            return lignes[i-1]
        i += 1
