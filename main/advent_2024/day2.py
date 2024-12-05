from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    reports_ok = 0
    for ligne in lignes:
        levels = [int(nb) for nb in ligne.split(" ")]
        if is_ok(levels):
            reports_ok += 1
    return reports_ok


def part2(input_path):
    lignes = lire_fichier(input_path)
    reports_ok = 0
    for ligne in lignes:
        levels = [int(nb) for nb in ligne.split(" ")]
        if is_ok(levels):
            reports_ok += 1
        else:
            for i in range(0, len(levels)):
                if is_ok_remove_one(levels, i):
                    reports_ok += 1
                    break
    return reports_ok


def is_ok(levels: list[int]):
    is_ascending = levels[0] < levels[1]
    ok = True
    if is_ascending:
        for a, b in zip(levels, levels[1:]):
            if not a < b:
                ok = False
                break
            if abs(b - a) > 3:
                ok = False
                break
    else:
        for a, b in zip(levels, levels[1:]):
            if not a > b:
                ok = False
                break
            if abs(b - a) > 3:
                ok = False
                break
    return ok


def is_ok_remove_one(levels: list[int], element_to_remove: int):
    return is_ok(levels[:element_to_remove] + levels[element_to_remove + 1:])
