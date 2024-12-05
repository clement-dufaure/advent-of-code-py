from main.utils.coord_utils import Coord
from main.utils.directions_utils import directions
from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    grid = {}
    nb_xmas_find = 0
    for y, ligne in enumerate(lignes):
        for x, lettre in enumerate(ligne):
            grid[Coord(x, y)] = lettre
    for case, lettre in grid.items():
        if lettre == "X":
            for direction in directions.values():
                if grid.get(case + direction) == "M" and grid.get(case + 2 * direction) == "A" and grid.get(
                        case + 3 * direction) == "S":
                    nb_xmas_find += 1
    return nb_xmas_find


def part2(input_path):
    lignes = lire_fichier(input_path)
    grid = {}
    nb_xmas_find = 0
    for y, ligne in enumerate(lignes):
        for x, lettre in enumerate(ligne):
            grid[Coord(x, y)] = lettre
    for case, lettre in grid.items():
        if lettre == "A":
            if check_cross(grid, case):
                nb_xmas_find += 1
    return nb_xmas_find


def check_cross(grid, coord_center) -> bool:
    check_ne_so = grid.get(coord_center + directions["NE"]) == "M" and grid.get(coord_center + directions["SO"]) == "S"
    check_so_ne = grid.get(coord_center + directions["SO"]) == "M" and grid.get(coord_center + directions["NE"]) == "S"
    check_no_se = grid.get(coord_center + directions["NO"]) == "M" and grid.get(coord_center + directions["SE"]) == "S"
    check_se_no = grid.get(coord_center + directions["SE"]) == "M" and grid.get(coord_center + directions["NO"]) == "S"
    return (check_ne_so or check_so_ne) and (check_no_se or check_se_no)
