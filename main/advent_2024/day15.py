from main.utils.coord_utils import Coord
from main.utils.directions_utils import directions
from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    grid: dict[Coord, str] = {}
    position = None
    y_global = 0
    for y, ligne in enumerate(lignes):
        y_global = y
        if ligne == "":
            break
        for x, char in enumerate(ligne):
            if char == "#":
                grid[Coord(x, y)] = "#"
            elif char == "O":
                grid[Coord(x, y)] = "O"
            elif char == "@":
                position = Coord(x, y)
    y_global += 1
    mouvements = "".join(lignes[y_global:])
    for mouvement in mouvements:
        direction = read_direction(mouvement)
        new_position = position + directions[direction]
        if new_position not in grid.keys():
            position = new_position
            continue
        # if wall do nothing
        # if box
        if grid[new_position] == "O":
            check = new_position
            while True:
                check = check + directions[direction]
                if check not in grid.keys():
                    # push boxes
                    grid[check] = "O"
                    grid.pop(new_position)
                    position = new_position
                    break
                if grid[check] == "O":
                    continue
                if grid[check] == "#":
                    break
    total = 0
    for coord in (k for k, v in grid.items() if v == "O"):
        total += 100 * coord.y + coord.x
    return total


def read_direction(input_char: str) -> str:
    if input_char == "^":
        return "N"
    if input_char == "v":
        return "S"
    if input_char == "<":
        return "O"
    if input_char == ">":
        return "E"


def part2(input_path, draw=False):
    lignes = lire_fichier(input_path)
    grid: dict[Coord, str] = {}
    position = None
    y_global = 0
    for y, ligne in enumerate(lignes):
        y_global = y
        if ligne == "":
            break
        for x, char in enumerate(ligne):
            if char == "#":
                grid[Coord(2 * x, y)] = "#"
                grid[Coord(2 * x + 1, y)] = "#"
            elif char == "O":
                grid[Coord(2 * x, y)] = "["
                grid[Coord(2 * x + 1, y)] = "]"
            elif char == "@":
                position = Coord(2 * x, y)
    y_size = y_global
    y_global += 1
    mouvements = "".join(lignes[y_global:])
    for mouvement in mouvements:
        if draw:
            draw_grid(grid, position, 2 * len(lignes[0]), y_size)
        direction = read_direction(mouvement)
        new_position = position + directions[direction]
        if new_position not in grid.keys():
            position = new_position
            continue
        # if wall do nothing
        # if box
        if grid[new_position] == "[" or grid[new_position] == "]":
            if direction == "E" or direction == "O":
                check = new_position
                cases_involved = []
                while True:
                    cases_involved.append(check)
                    cases_involved.append(check + directions[direction])
                    check = check + 2 * directions[direction]
                    if check not in grid.keys():
                        # push boxes
                        push_boxes(cases_involved, direction, grid)
                        position = new_position
                        break
                    if grid[check] == "O":
                        continue
                    if grid[check] == "#":
                        break
            if direction == "N" or direction == "S":
                check = new_position
                cases_involved = set()
                last_cases_involved = set()
                last_cases_involved.add(check)
                consolider(grid, last_cases_involved)
                bloque = False
                while not bloque:
                    cases_involved.update(last_cases_involved)
                    next_cases_involved = set()
                    for case in last_cases_involved:
                        if case + directions[direction] not in grid.keys():
                            continue
                        elif grid[case + directions[direction]] == "#":
                            bloque = True
                            break
                        elif grid[case + directions[direction]] == "[" or grid[case + directions[direction]] == "]":
                            next_cases_involved.add(case + directions[direction])
                        else:
                            raise "error"
                    if len(next_cases_involved) > 0 and not bloque:
                        consolider(grid, next_cases_involved)
                        last_cases_involved = next_cases_involved
                    elif len(next_cases_involved) == 0 and not bloque:
                        push_boxes(cases_involved, direction, grid)
                        position = new_position
                        break
    total = 0
    for coord in (k for k, v in grid.items() if v == "["):
        total += 100 * coord.y + coord.x
    return total


def consolider(grid: dict, cases_involved: set):
    new_cases = []
    for case in cases_involved:
        if grid[case] == "[":
            new_cases.append(case + directions["E"])
        elif grid[case] == "]":
            new_cases.append(case + directions["O"])
        else:
            raise "error"
    cases_involved.update(new_cases)


def push_boxes(cases_involved, direction, grid):
    modifications = {}
    for case in cases_involved:
        old = grid[case]
        new_key = case + directions[direction]
        modifications[new_key] = old
    for case in cases_involved:
        grid.pop(case, None)
    grid.update(modifications)


def draw_grid(grid: dict, pos: Coord, max_x, max_y):
    out = ""
    for y in range(max_y):
        for x in range(max_x):
            if Coord(x, y) in grid.keys():
                out += grid[Coord(x, y)]
            elif pos == Coord(x, y):
                out += "@"
            else:
                out += "."
        out += "\n"
    print(out)
