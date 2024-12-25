from heapq import heappush, heappop

from main.utils.coord_utils import Coord
from main.utils.directions_utils import directions
from main.utils.files_utils import lire_fichier


class Path:

    def __init__(self, last: Coord,
                 # path: set[Coord],
                 score: int,
                 state_cheat=0):
        self.last = last
        # self.path = path
        self.score = score
        self.state_cheat = state_cheat

    def __lt__(self, other):
        return self.score < other.score


orientations = ["N", "E", "S", "O"]


def part1(input_path, min_raccourci=100):
    lignes = lire_fichier(input_path)
    walls: set[Coord] = set()
    start = None
    end = None
    for y, ligne in enumerate(lignes):
        for x, lettre in enumerate(ligne):
            if lettre == "#":
                walls.add(Coord(x, y))
            if lettre == "S":
                start = Coord(x, y)
            if lettre == "E":
                end = Coord(x, y)
    race_path: dict[Coord, int] = {}
    current = start
    index = 0
    while True:
        race_path[current] = index
        if current == end:
            break
        for direction in orientations:
            new_case = current + directions[direction]
            # if wall do nothing or out of bounds
            # if already in path do nothing
            if new_case not in walls and new_case not in race_path.keys():
                index += 1
                current = new_case
                break
    # recherche raccourcis
    cheats = {}
    nb_raccourci = 0
    for case in race_path:
        for direction in orientations:
            new_case = case + directions[direction]
            if new_case in walls:
                for direction2 in orientations:
                    new_case2 = new_case + directions[direction2]
                    if new_case2 != case and new_case2 in race_path:
                        raccourci_value = race_path[new_case2] - race_path[case] - 2
                        if raccourci_value >= min_raccourci:
                            cheats[(case, new_case2)] = raccourci_value
                            nb_raccourci += 1
    return nb_raccourci


def part2(input_path, min_raccourci=100, picoseconds_cheat=20):
    lignes = lire_fichier(input_path)
    walls: set[Coord] = set()
    start = None
    end = None
    for y, ligne in enumerate(lignes):
        for x, lettre in enumerate(ligne):
            if lettre == "#":
                walls.add(Coord(x, y))
            if lettre == "S":
                start = Coord(x, y)
            if lettre == "E":
                end = Coord(x, y)
    race_path: dict[Coord, int] = {}
    current = start
    index = 0
    while True:
        race_path[current] = index
        if current == end:
            break
        for direction in orientations:
            new_case = current + directions[direction]
            # if wall do nothing or out of bounds
            # if already in path do nothing
            if new_case not in walls and new_case not in race_path.keys():
                index += 1
                current = new_case
                break
    # recherche raccourcis
    nb_raccourci = 0
    for case in race_path:
        print(f"{race_path[case]} of {len(race_path)}")
        cases_a_atteindre = {coord for coord, index in race_path.items() if index - race_path[case] >= min_raccourci}
        for try_case in cases_a_atteindre:
            manhatan_distance = abs(case.x - try_case.x) + abs(case.y - try_case.y)
            # check temps d'y arriver et vraiment un raccourci
            if manhatan_distance <= picoseconds_cheat \
                    and race_path[try_case] - race_path[case] - manhatan_distance >= min_raccourci:
                nb_raccourci += 1
    return nb_raccourci
