from main.utils.coord_utils import Coord
from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    keys = []
    locks = []
    object_en_cours = []
    on_change = True
    y_en_cours = 0
    is_key = True
    for ligne in lignes:
        if ligne == "":
            on_change = True
            if is_key:
                keys.append(object_en_cours)
            else:
                locks.append(object_en_cours)
            object_en_cours = []
        else:
            if on_change:
                # begin new object
                is_key = ligne[0] == "."
                y_en_cours = 6 if is_key else 0
                on_change = False
            for x, lettre in enumerate(ligne):
                if lettre == "#":
                    object_en_cours.append(Coord(x, y_en_cours))
            if is_key:
                y_en_cours -= 1
            else:
                y_en_cours += 1
    if is_key:
        keys.append(object_en_cours)
    else:
        locks.append(object_en_cours)
    locks_schemes = []
    key_schemes = []
    for lock in locks:
        current = []
        for x in range(5):
            for y in range(7):
                if Coord(x, y) not in lock:
                    current.append(y - 1)
                    break
        locks_schemes.append(current)
    for key in keys:
        current = []
        for x in range(5):
            for y in range(7):
                if Coord(x, y) not in key:
                    current.append(y - 1)
                    break
        key_schemes.append(current)
    nb_matches = 0
    for key in key_schemes:
        for lock in locks_schemes:
            ok = True
            for x in range(5):
                if key[x] + lock[x] > 5:
                    ok = False
                    break
            if ok:
                nb_matches += 1
    return nb_matches


def part2(input_path):
    lignes = lire_fichier(input_path)
