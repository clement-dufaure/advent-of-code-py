from typing import Type

from main.utils.coord_utils import Coord
from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    antennas: dict[str, list[Coord]] = {}
    for y, ligne in enumerate(lignes):
        for x, lettre in enumerate(ligne):
            if not lettre == ".":
                if lettre in antennas.keys():
                    antennas[lettre].append(Coord(x, y))
                else:
                    antennas[lettre] = [Coord(x, y)]
    max_y = len(lignes)
    max_x = len(lignes[0])
    antinode_points: set[Coord] = set()
    for antennas_signal in antennas.values():
        for i, antenna1 in enumerate(antennas_signal):
            for antenna2 in antennas_signal[i + 1:]:
                ecart = antenna2 - antenna1
                antenode1 = antenna1 - ecart
                antenode2 = antenna2 + ecart
                if 0 <= antenode1.x < max_x and 0 <= antenode1.y < max_y:
                    antinode_points.add(antenode1)
                if 0 <= antenode2.x < max_x and 0 <= antenode2.y < max_y:
                    antinode_points.add(antenode2)
    return len(antinode_points)


def part2(input_path):
    lignes = lire_fichier(input_path)
    antennas: dict[str, list[Coord]] = {}
    for y, ligne in enumerate(lignes):
        for x, lettre in enumerate(ligne):
            if not lettre == ".":
                if lettre in antennas.keys():
                    antennas[lettre].append(Coord(x, y))
                else:
                    antennas[lettre] = [Coord(x, y)]
    max_y = len(lignes)
    max_x = len(lignes[0])
    antinode_points: set[Coord] = set()
    for antennas_signal in antennas.values():
        for i, antenna1 in enumerate(antennas_signal):
            for antenna2 in antennas_signal[i + 1:]:
                ecart = antenna2 - antenna1
                antenode1 = antenna1
                while True:
                    if 0 <= antenode1.x < max_x and 0 <= antenode1.y < max_y:
                        antinode_points.add(antenode1)
                        antenode1 = antenode1 - ecart
                    else:
                        break
                antenode2 = antenna2
                while True:
                    if 0 <= antenode2.x < max_x and 0 <= antenode2.y < max_y:
                        antinode_points.add(antenode2)
                        antenode2 = antenode2 + ecart
                    else:
                        break
    return len(antinode_points)
