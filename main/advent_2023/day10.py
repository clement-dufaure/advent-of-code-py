from enum import Enum

from main.utils.coord_utils import Coord
from main.utils.files_utils import lire_fichier


class Direction(Enum):
    NORTH = Coord(0, -1)
    SOUTH = Coord(0, 1)
    EAST = Coord(1, 0)
    WEST = Coord(-1, 0)


opposites = {
    Direction.NORTH: Direction.SOUTH,
    Direction.SOUTH: Direction.NORTH,
    Direction.EAST: Direction.WEST,
    Direction.WEST: Direction.EAST
}


def lire_input(grid_lines: list[str]) -> dict[Coord, str]:
    grid_dict = {}
    for row_index, row in enumerate(grid_lines):
        for col_index, value in enumerate(row):
            coord = Coord(col_index, row_index)
            grid_dict[coord] = value
    return grid_dict


exits = {
    "|": [Direction.NORTH, Direction.SOUTH],
    "-": [Direction.EAST, Direction.WEST],
    "L": [Direction.NORTH, Direction.EAST],
    "J": [Direction.NORTH, Direction.WEST],
    "7": [Direction.SOUTH, Direction.WEST],
    "F": [Direction.SOUTH, Direction.EAST],
    ".": []
}


def get_start_direction(start_coord: Coord, grid: dict[Coord, str]) -> Direction:
    for direction in Direction:
        case_value = grid.get(Coord(start_coord.x + direction.value.x, start_coord.y + direction.value.y), ".")
        if case_value != "." and opposites.get(direction) in exits.get(case_value):
            return direction


def get_direction_exit(case: Coord, direction_from: Direction, grid: dict[Coord, str]) -> Direction:
    return next(direction for direction in exits.get(grid.get(case)) if direction != opposites.get(direction_from))


def compute_path(grid: dict[Coord, str], start: Coord):
    direction = get_start_direction(start, grid)
    case = Coord(start.x + direction.value.x, start.y + direction.value.y)
    chemin: list[Coord] = [start]
    while case != start:
        chemin.append(case)
        direction = get_direction_exit(case, direction, grid)
        case = Coord(case.x + direction.value.x, case.y + direction.value.y)
    return chemin


def get_start_real_pipe(grid, start: Coord):
    direction_connectees = []
    for direction in Direction:
        case_value = grid.get(Coord(start.x + direction.value.x, start.y + direction.value.y), ".")
        if case_value != "." and opposites.get(direction) in exits.get(case_value):
            direction_connectees.append(direction)
    for key, value in exits.items():
        if value == direction_connectees:
            return key


def part1(input_path) -> int:
    grid = lire_input(lire_fichier(input_path))
    start = next(key for key, value in grid.items() if value == "S")
    chemin = compute_path(grid, start)
    return len(chemin) // 2


def calculer_aire(grid: dict[Coord, str], chemin: list[Coord]):
    ordonnees = [coord.y for coord in chemin]
    abscisses = [coord.x for coord in chemin]
    min_x = min(abscisses)
    max_x = max(abscisses)
    chemin = sorted(chemin, key=lambda coord: (coord.y, coord.x), reverse=True)
    next_coord_chemin = chemin.pop()
    aire = 0
    for j in range(min(ordonnees), max(ordonnees) + 1):
        interieur = False
        direction_angle = None
        for i in range(min_x, max_x + 1):
            coord = Coord(i, j)
            if coord == next_coord_chemin:
                if chemin:
                    next_coord_chemin = chemin.pop()
                pipe = grid.get(coord)
                if pipe == "-":
                    continue
                if pipe == "|":
                    interieur = not interieur
                    continue
                direction_angle_courant = Direction.NORTH if Direction.NORTH in exits.get(pipe) else Direction.SOUTH
                # angle
                if direction_angle is None:
                    direction_angle = direction_angle_courant
                else:
                    if direction_angle_courant != direction_angle:
                        interieur = not interieur
                    direction_angle = None
            else:
                if interieur:
                    aire += 1
    return aire


def part2(input_path) -> int:
    grid = lire_input(lire_fichier(input_path))
    start = next(key for key, value in grid.items() if value == "S")
    real_pipe = get_start_real_pipe(grid, start)
    grid[start] = real_pipe
    chemin = compute_path(grid, start)
    return calculer_aire(grid, chemin)
