import re

from main.utils.files_utils import lire_fichier


def determiner_suite(serie: list[int]) -> int:
    lasts: list[int] = []
    while any(item != 0 for item in serie):
        lasts.append(serie[-1])
        serie = [serie[i + 1] - serie[i] for i in range(len(serie) - 1)]
    return sum(lasts)


def determiner_precedent(serie: list[int]) -> int:
    firsts: list[int] = []
    while any(item != 0 for item in serie):
        firsts.append(serie[0])
        serie = [serie[i + 1] - serie[i] for i in range(len(serie) - 1)]
    precedent = 0
    for first in reversed(firsts):
        precedent = first - precedent
    return precedent


def part1(input_path):
    suites: list[int] = []
    for ligne in lire_fichier(input_path):
        serie = list(map(int, re.findall(r"(-?\d+)", ligne)))
        suites.append(determiner_suite(serie))
    return sum(suites)


def part2(input_path):
    precedents: list[int] = []
    for ligne in lire_fichier(input_path):
        serie = list(map(int, re.findall(r"(-?\d+)", ligne)))
        precedents.append(determiner_precedent(serie))
    return sum(precedents)
