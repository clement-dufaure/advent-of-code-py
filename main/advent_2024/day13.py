import re
from itertools import product

from main.utils.files_utils import lire_fichier

pattern = r"Button A: X\+(\d+), Y\+(\d+)Button B: X\+(\d+), Y\+(\d+)Prize: X=(\d+), Y=(\d+)"


class ClawMachine:

    def __init__(self, ax: int, ay: int, bx: int, by: int, px: int, py: int):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.px = px
        self.py = py


def part1(input_path):
    lignes = lire_fichier(input_path)
    all_input = "".join(lignes)
    machines: list[ClawMachine] = []
    for result in re.findall(pattern, all_input):
        machines.append(
            ClawMachine(int(result[0]), int(result[1]), int(result[2]), int(result[3]), int(result[4]), int(result[5])))
    combs = list(product(range(100), range(100)))
    total_token = 0
    nb_prix = 0
    for machine in machines:
        for comb in combs:
            test_x = comb[0] * machine.ax + comb[1] * machine.bx
            test_y = comb[0] * machine.ay + comb[1] * machine.by
            if test_x == machine.px and test_y == machine.py:
                total_token += 3 * comb[0] + comb[1]
                nb_prix += 1
    return total_token


def part2(input_path):
    lignes = lire_fichier(input_path)
    all_input = "".join(lignes)
    machines: list[ClawMachine] = []
    for result in re.findall(pattern, all_input):
        offset = 10000000000000
        machines.append(
            ClawMachine(int(result[0]), int(result[1]), int(result[2]), int(result[3]), int(result[4]) + offset,
                        int(result[5]) + offset))
    total_token = 0
    nb_prix = 0
    for machine in machines:
        # ax * comb_a + bx * comb_b = px
        # ay * comb_a + by * comb_b = py
        # comb_b = (px - ax * comb_a) / bx
        # det = ax * by - bx * ay
        # comb_a = (by * px - bx * py) / det
        # comb_b = (ax * py - ay * px) / det
        det = machine.ax * machine.by - machine.bx * machine.ay
        if not det == 0:
            comb_a = (machine.by * machine.px - machine.bx * machine.py) / det
            comb_b = (machine.ax * machine.py - machine.ay * machine.px) / det
            if comb_a.is_integer() and comb_b.is_integer() and comb_a >= 0 and comb_b >= 0:
                total_token += 3 * int(comb_a) + int(comb_b)
                nb_prix += 1
    return total_token
