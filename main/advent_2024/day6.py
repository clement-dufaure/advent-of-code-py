from main.utils.coord_utils import Coord
from main.utils.directions_utils import directions
from main.utils.files_utils import lire_fichier
from main.utils.walk_utils import Walk


def part1(input_path):
    lignes = lire_fichier(input_path)
    obstructions = set()
    parcours = set()
    position = Coord(0, 0)
    direction = "N"
    max_x = len(lignes[0])
    max_y = len(lignes)
    for y, ligne in enumerate(lignes):
        for x, case in enumerate(ligne):
            if case == "#":
                obstructions.add(Coord(x, y))
            if case == "^":
                position = Coord(x, y)
    while 0 <= position.x < max_x and 0 <= position.y < max_y:
        parcours.add(position)
        front = position + directions.get(direction)
        if front in obstructions:
            direction = rotate(direction)
        else:
            position = front
    return len(parcours)


def rotate(direction):
    if direction == "N":
        return "E"
    if direction == "E":
        return "S"
    if direction == "S":
        return "O"
    if direction == "O":
        return "N"


def part2(input_path):
    lignes = lire_fichier(input_path)
    obstructions = set()
    parcours = set()
    start = Coord(0, 0)
    direction = "N"
    max_x = len(lignes[0])
    max_y = len(lignes)
    for y, ligne in enumerate(lignes):
        for x, case in enumerate(ligne):
            if case == "#":
                obstructions.add(Coord(x, y))
            if case == "^":
                start = Coord(x, y)
    position = start
    while 0 <= position.x < max_x and 0 <= position.y < max_y:
        parcours.add(position)
        front = position + directions.get(direction)
        if front in obstructions:
            direction = rotate(direction)
        else:
            position = front
    nb_loop = 0
    parcours.remove(start)
    for i, new_obstruction in enumerate(parcours):
        print(f"check {i} of {len(parcours)}")
        obstructions.add(new_obstruction)
        if parcours_has_loop(start, obstructions, max_x, max_y):
            nb_loop += 1
        obstructions.remove(new_obstruction)
    return nb_loop


def parcours_has_loop(position: Coord, obstructions: set[Coord], max_x, max_y):
    walks = set()
    direction = "N"
    loop = False
    while 0 <= position.x < max_x and 0 <= position.y < max_y:
        walk = Walk(position, direction)
        if walk in walks:
            loop = True
            break
        walks.add(walk)
        front = position + directions.get(direction)
        if front in obstructions:
            direction = rotate(direction)
        else:
            position = front
    return loop
