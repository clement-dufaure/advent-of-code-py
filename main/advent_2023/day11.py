from main.utils.coord_utils import Coord
from main.utils.files_utils import lire_fichier


def get_rows_to_expand(lignes: list[str]) -> list[int]:
    rows_to_expand = []
    for i, ligne in enumerate(lignes):
        if "#" not in ligne:
            rows_to_expand.append(i)
    return rows_to_expand


def get_colums_to_expand(lignes: list[str]) -> list[int]:
    taille_ligne = len(lignes[0])
    is_colum_to_expand = [True] * taille_ligne
    colums_to_expand = []
    for ligne in lignes:
        for i, c in enumerate(ligne):
            if c == "#":
                is_colum_to_expand[i] = False
    for i, to_expand in enumerate(is_colum_to_expand):
        if to_expand:
            colums_to_expand.append(i)
    return colums_to_expand


def distance_manhattan(coord1: Coord, coord2: Coord) -> int:
    return abs(coord1.x - coord2.x) + abs(coord1.y - coord2.y)


def distance_manhattan_with_expand(coord1: Coord, coord2: Coord, rows_to_expand: list[int],
                                   colums_to_expand: list[int], coeff_expand: int) -> int:
    expand_x = 0
    expand_y = 0
    for row in rows_to_expand:
        if min(coord1.y, coord2.y) < row < max(coord1.y, coord2.y):
            expand_x += coeff_expand - 1
    for column in colums_to_expand:
        if min(coord1.x, coord2.x) < column < max(coord1.x, coord2.x):
            expand_y += coeff_expand - 1
    return distance_manhattan(coord1, coord2) + expand_x + expand_y


def compute_distances(lignes: list[str], coeff: int) -> int:
    rows_to_expand = get_rows_to_expand(lignes)
    colums_to_expand = get_colums_to_expand(lignes)
    galaxies = [Coord(j, i) for i, ligne in enumerate(lignes) for j, c in enumerate(ligne) if c == "#"]
    somme = 0
    for i, galaxie1 in enumerate(galaxies):
        for galaxie2 in galaxies[i + 1:]:
            somme += distance_manhattan_with_expand(galaxie1, galaxie2, rows_to_expand, colums_to_expand, coeff)
    return somme


def part1(input_path):
    return compute_distances(lire_fichier(input_path), 2)


def part2(input_path, coeff=None):
    return compute_distances(lire_fichier(input_path), 1000000 if coeff is None else coeff)
