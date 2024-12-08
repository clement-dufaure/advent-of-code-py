from itertools import product

from main.utils.files_utils import lire_fichier


class Equation:

    def __init__(self, result: int, operandes: list[int]):
        self.result = result
        self.operandes = operandes


def part1(input_path):
    lignes = lire_fichier(input_path)
    equations: list[Equation] = []
    for ligne in lignes:
        s = ligne.split(": ")
        o = list(map(int, s[1].split(" ")))
        equations.append(Equation(int(s[0]), o))
    total = 0
    for equation in equations:
        if is_equation_ok(equation, [somme, multiply]):
            total += equation.result
    return total


def part2(input_path):
    lignes = lire_fichier(input_path)
    equations: list[Equation] = []
    for ligne in lignes:
        s = ligne.split(": ")
        o = list(map(int, s[1].split(" ")))
        equations.append(Equation(int(s[0]), o))
    total = 0
    for i, equation in enumerate(equations):
        print(f"equation {i} of {len(equations)}")
        if is_equation_ok(equation, [somme, multiply, concatenate]):
            total += equation.result
    return total


def is_equation_ok(equation: Equation, operators: []):
    combinaisons = list(product(operators, repeat=len(equation.operandes) - 1))
    for combinaison in combinaisons:
        test_result = equation.operandes[0]
        for i, operator in enumerate(combinaison):
            test_result = operator(test_result, equation.operandes[i + 1])
        if test_result == equation.result:
            return True
    return False


def somme(a, b):
    return a + b


def multiply(a, b):
    return a * b


def concatenate(a, b):
    return int(str(a) + str(b))
