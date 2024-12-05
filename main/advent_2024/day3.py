import re

from main.utils.files_utils import lire_fichier

regex = r"mul\((\d{1,3}),(\d{1,3})\)"
regex2 = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"


def part1(input_path):
    lignes = lire_fichier(input_path)
    total = 0
    for ligne in lignes:
        all_mul: list[tuple] = re.findall(regex, ligne)
        for mul in all_mul:
            total += int(mul[0]) * int(mul[1])
    return total


def part2(input_path):
    lignes = lire_fichier(input_path)
    total = 0
    enabled = True
    for ligne in lignes:
        all_mul: list[tuple] = re.findall(regex2, ligne)
        for mul in all_mul:
            if mul[2]:
                enabled = True
            elif mul[3]:
                enabled = False
            else:
                if enabled:
                    total += int(mul[0]) * int(mul[1])
    return total
