from main.utils.coord_utils import Coord
from main.utils.directions_utils import directions
from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    ranges = []
    ingredient = []
    nb_fresh = 0
    for ligne in lignes:
        if "-" in ligne:
            sp = ligne.split("-")
            ranges.append((int(sp[0]), int(sp[1])))
        elif ligne != "":
            ingredient.append(int(ligne))
    for i in ingredient:
        for r in ranges:
            if r[0] <= i <= r[1]:
                nb_fresh += 1
                break
    return nb_fresh


def part2(input_path):
    lignes = lire_fichier(input_path)
    bornes: dict[int, list[int]] = {}
    nb_fresh = 0
    for ligne in lignes:
        if "-" in ligne:
            sp = ligne.split("-")
            bornes[int(sp[0])] = bornes.get(int(sp[0]), []) + [1]
            bornes[int(sp[1])] = bornes.get(int(sp[1]), []) + [-1]
    bornes_sorted = sorted(bornes.keys())
    current = 0
    inside = False
    depth = 0
    for borne in bornes_sorted:
        if inside:
            nb_fresh += borne - current
        if not inside and 1 in bornes[borne]:
            nb_fresh += 1
        depth += sum(bornes[borne])
        if depth > 0:
            inside = True
        if depth == 0:
            inside = False
        current = borne
    return nb_fresh
