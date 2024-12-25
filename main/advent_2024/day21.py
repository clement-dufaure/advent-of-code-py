from main.utils.coord_utils import Coord
from main.utils.directions_utils import directions
from main.utils.files_utils import lire_fichier

numeric_pad = {
    "0": Coord(1, 3),
    "1": Coord(0, 2),
    "2": Coord(1, 2),
    "3": Coord(2, 2),
    "4": Coord(0, 1),
    "5": Coord(1, 1),
    "6": Coord(2, 1),
    "7": Coord(0, 0),
    "8": Coord(1, 0),
    "9": Coord(2, 0),
    "A": Coord(2, 3),
}

reverted_numeric_pad = {value: key for key, value in numeric_pad.items()}

directional_pad = {
    "N": Coord(1, 0),
    "E": Coord(2, 1),
    "O": Coord(0, 1),
    "S": Coord(1, 1),
    "A": Coord(2, 0),
}

reverted_directional_pad = {value: key for key, value in directional_pad.items()}


def part1(input_path, nb_pads=2):
    codes = lire_fichier(input_path)
    paths = {}
    for c, code in enumerate(codes):
        paths_ok = find_best_paths(numeric_pad["A"], code, numeric_pad, reverted_numeric_pad)
        lengths = []
        for path in paths_ok:
            length = 0
            unitaires = path.split("A")
            for u in unitaires[:-1]:
                length += find_size_directional_path(u + "A", nb_pads)
            lengths.append(length)
        paths[code] = min(lengths)
    total = 0
    for code in paths:
        total += int(code[:-1]) * paths[code]
    return total


memoire = {}


def find_size_directional_path(path, nb_pad):
    if nb_pad == 0:
        return len(path)

    if (path, nb_pad) in memoire:
        return memoire[(path, nb_pad)]

    paths_ok = find_best_paths(directional_pad["A"], path, directional_pad, reverted_directional_pad)
    lengths = []
    for path_ok in paths_ok:
        length = 0
        unitaires = path_ok.split("A")
        for u in unitaires[:-1]:
            length += find_size_directional_path(u + "A", nb_pad - 1)
        lengths.append(length)

    resultat = min(lengths)
    memoire[(path, nb_pad)] = resultat
    return resultat


def find_next_paths(start: Coord, end: Coord, reverted_pave: dict[Coord, str]):
    direction_x = "O" if start.x >= end.x else "E"
    distance_x = abs(start.x - end.x)
    direction_y = "N" if start.y >= end.y else "S"
    distance_y = abs(start.y - end.y)
    paths = set()
    # verif coins
    if start + directions[direction_x] * distance_x in reverted_pave:
        paths.add(direction_x * distance_x + direction_y * distance_y + "A")
    if start + directions[direction_y] * distance_y in reverted_pave:
        paths.add(direction_y * distance_y + direction_x * distance_x + "A")
    return paths


def find_best_paths(global_start: Coord, code_attendu: str, pave: dict[str, Coord], reverted_pave: dict[Coord, str]):
    paths = {""}
    start = global_start
    for c in code_attendu:
        end = pave[c]
        new_paths = set()
        for next_path in find_next_paths(start, end, reverted_pave):
            for current_path in paths:
                new_paths.add(current_path + next_path)
        paths = new_paths
        start = end
    return paths
