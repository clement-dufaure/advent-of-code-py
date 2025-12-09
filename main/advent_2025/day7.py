from main.utils.coord_utils import Coord
from main.utils.files_utils import lire_fichier, lire_fichier_no_strip
from math import prod


def part1(input_path):
    lignes = lire_fichier(input_path)
    beams = set()
    row_splitters = [[] for _ in range(len(lignes))]
    for i, ligne in enumerate(lignes):
        for j, char in enumerate(ligne):
            if char == "S":
                beams.add(j)
            if char == "^":
                row_splitters[i].append(j)
    nb_splitters_hit = 0
    for splitters in row_splitters:
        new_beams = set()
        for beam in beams:
            if beam in splitters:
                nb_splitters_hit += 1
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
            else:
                new_beams.add(beam)
        beams = new_beams
    return nb_splitters_hit


def part2(input_path):
    lignes = lire_fichier(input_path)
    row_splitters = [[] for _ in range(len(lignes))]
    start = None
    for i, ligne in enumerate(lignes):
        for j, char in enumerate(ligne):
            if char == "S":
                start = Coord(j, i)
            if char == "^":
                row_splitters[i].append(j)
    return how_many_timelines(start, row_splitters)


memory = {}


def how_many_timelines(start: Coord, row_splitters):
    if start in memory:
        return memory[start]
    if start.y + 1 == len(row_splitters):
        return 1
    if start.x not in row_splitters[start.y + 1]:
        result = how_many_timelines(Coord(start.x, start.y + 1), row_splitters)
        memory[start] = result
        return result
    else:
        result = how_many_timelines(Coord(start.x + 1, start.y + 1), row_splitters) + how_many_timelines(
            Coord(start.x - 1, start.y + 1), row_splitters)
        memory[start] = result
        return result
