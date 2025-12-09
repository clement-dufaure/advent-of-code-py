from main.utils.files_utils import lire_fichier, lire_fichier_no_strip
from math import prod


def part1(input_path):
    lignes = lire_fichier(input_path)
    numbers = [[] for _ in range(len(lignes[0].split()))]
    ops: list[str] = []
    for ligne in lignes:
        if ligne[0] == "+" or ligne[0] == "*":
            ops = ligne.split()
        else:
            numbers_ligne = ligne.split()
            for i, number in enumerate(numbers_ligne):
                numbers[i].append(int(number))
    return sum([compute(numbers[i], op) for i, op in enumerate(ops)])


def part2(input_path):
    lignes = lire_fichier_no_strip(input_path)
    lignes_numbers = lignes[:-1]
    max_len = max([len(ligne) for ligne in lignes_numbers])
    ops = lignes[-1].split()
    current_op_index = 0
    current_index = 0
    total = 0
    numbers_to_compute = []
    while current_index < max_len:
        current_number = ""
        for ligne in lignes_numbers:
            current_number += ligne.ljust(max_len)[current_index]
        if not current_number.strip() == "":
            numbers_to_compute.append(int(current_number))
        else:
            total += compute(numbers_to_compute, ops[current_op_index])
            numbers_to_compute = []
            current_op_index += 1
        current_index += 1
    total += compute(numbers_to_compute, ops[current_op_index])
    return total


def compute(numbers, op):
    if op == "+":
        return sum(numbers)
    if op == "*":
        return prod(numbers)
