from main.utils.coord_utils import Coord
from main.utils.directions_utils import directions
from main.utils.files_utils import lire_fichier

directions_possibles = ["N", "E", "S", "O"]


def part1(input_path):
    lignes = lire_fichier(input_path)
    grid: dict[Coord, int] = {}
    starts: list[Coord] = []
    for y, ligne in enumerate(lignes):
        for x, chiffre in enumerate(ligne):
            grid[Coord(x, y)] = int(chiffre)
            if chiffre == "0":
                starts.append(Coord(x, y))
    score = 0
    for start in starts:
        path = set()
        new_cases = []
        path.add(start)
        new_cases.append(start)
        nb_finish = 0
        while len(new_cases) > 0:
            case = new_cases.pop()
            level = grid[case]
            for direction in directions_possibles:
                to_check = case + directions[direction]
                if to_check in grid.keys():
                    new_level = grid[to_check]
                    if new_level - level == 1:
                        if to_check not in path:
                            path.add(to_check)
                            new_cases.append(to_check)
                            if new_level == 9:
                                nb_finish += 1
        score += nb_finish
    return score


def part2(input_path):
    lignes = lire_fichier(input_path)
    grid: dict[Coord, int] = {}
    starts: list[Coord] = []
    for y, ligne in enumerate(lignes):
        for x, chiffre in enumerate(ligne):
            grid[Coord(x, y)] = int(chiffre)
            if chiffre == "0":
                starts.append(Coord(x, y))
    total = 0
    for start in starts:
        score = 0
        pathes: list[list[Coord]] = [[start]]
        while len(pathes) > 0:
            path = pathes.pop()
            last = path[-1]
            level = grid[last]
            if level == 9:
                score += 1
            else:
                possible_next: list[Coord] = []
                for direction in directions_possibles:
                    to_check = last + directions[direction]
                    if to_check in grid.keys():
                        new_level = grid[to_check]
                        if new_level - level == 1:
                            possible_next.append(to_check)
                for next_case in possible_next:
                    pathes.append(path + [next_case])
        total += score
    return total
