from main.utils.coord_utils import Coord
from main.utils.directions_utils import directions
from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    rolls: set[Coord] = set()
    for i, ligne in enumerate(lignes):
        for j, case in enumerate(ligne):
            if case == "@":
                rolls.add(Coord(j, i))
    new_rolls = one_step(rolls)
    return len(rolls) - len(new_rolls)


def part2(input_path):
    lignes = lire_fichier(input_path)
    init_rolls: set[Coord] = set()
    for i, ligne in enumerate(lignes):
        for j, case in enumerate(ligne):
            if case == "@":
                init_rolls.add(Coord(j, i))
    new_rolls = init_rolls.copy()
    again = True
    while again:
        new_new_rolls = one_step(new_rolls)
        if len(new_new_rolls) == len(new_rolls):
            again = False
        else:
            new_rolls = new_new_rolls
    return len(init_rolls) - len(new_rolls)


def one_step(rolls: set[Coord]) -> set[Coord]:
    new_rolls = rolls.copy()
    rolls_to_pop = []
    for coord in rolls:
        count = 0
        for direction in directions:
            if Coord(coord.x + directions[direction].x, coord.y + directions[direction].y) in rolls:
                count += 1
        if count < 4:
            rolls_to_pop.append(coord)
    for roll in rolls_to_pop:
        new_rolls.remove(roll)
    return new_rolls
