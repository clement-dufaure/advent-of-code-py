from shapely import Polygon

from main.utils.coord_utils import Coord
from main.utils.files_utils import lire_fichier


def part1(input_path, nb_iterations):
    lignes = lire_fichier(input_path)
    coords = []
    for ligne in lignes:
        s = ligne.split(",")
        coords.append(Coord(int(s[0]), int(s[1])))
    my_max = 0
    for coord1 in coords:
        for coord2 in coords:
            aire = (abs(coord1.x - coord2.x) + 1) * (abs(coord1.y - coord2.y) + 1)
            if aire > my_max:
                my_max = aire
    return my_max


def part2(input_path):
    lignes = lire_fichier(input_path)
    size = len(lignes)
    print(f"size : {size}")
    coords = []
    for ligne in lignes:
        s = ligne.split(",")
        coords.append((int(s[0]), int(s[1])))
    p = Polygon(coords)
    my_max = 0
    for a, coord1 in enumerate(coords):
        for b, coord2 in enumerate(coords):
            print(f"Check ({a},{b})")
            rect = Polygon([coord1, (coord1[0], coord2[1]), coord2, (coord2[0], coord1[1])])
            aire = (abs(coord1[0] - coord2[0]) + 1) * (abs(coord1[1] - coord2[1]) + 1)
            if aire > my_max and rect.within(p):
                my_max = aire
    return my_max
