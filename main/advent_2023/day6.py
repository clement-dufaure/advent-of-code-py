import cmath
import math
import re
from functools import reduce

from main.utils.files_utils import lire_fichier
from main.utils.interval_util import Interval


def floor_or_inf(nombre: float) -> int:
    if nombre.is_integer():
        return int(nombre) - 1
    return math.floor(nombre)


def ceil_or_sup(nombre: float) -> int:
    if nombre.is_integer():
        return int(nombre) + 1
    return math.ceil(nombre)


def interval_time_to_hold_to_go_further(max_time: int, record: int) -> Interval:
    # distance_parcourue = hold_time * (max_time - hold_time)
    # resolve hold_time² - hold_time*max_time + record < 0
    # on admet que les solutions sont réelles et strictement incluses dans 0-max_time
    delta = max_time ** 2 - 4 * record
    solution1 = ((max_time - cmath.sqrt(delta)) / 2).real
    solution2 = ((max_time + cmath.sqrt(delta)) / 2).real
    return Interval(ceil_or_sup(solution1), floor_or_inf(solution2))


def part1(input_path) -> int:
    times_str, distances_str = lire_fichier(input_path)
    times = list(map(int, re.findall(r"(\d+)", times_str)))
    distances = list(map(int, re.findall(r"(\d+)", distances_str)))
    data = list(zip(times, distances))
    marges: list[int] = []
    for race in data:
        interval = interval_time_to_hold_to_go_further(race[0], race[1])
        marges.append(interval.length() + 1)
    return reduce((lambda x, y: x * y), marges)


def part2(input_path) -> int:
    times_str, distances_str, *autres = lire_fichier(input_path)
    time = int(re.findall(r"(\d+)", times_str.replace(" ", ""))[0])
    distance = int(re.findall(r"(\d+)", distances_str.replace(" ", ""))[0])
    return interval_time_to_hold_to_go_further(time, distance).length() + 1
