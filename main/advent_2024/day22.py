from itertools import product

from main.utils.files_utils import lire_fichier


def part1(input_path):
    step = list(map(int, lire_fichier(input_path)))
    for _ in range(2000):
        next_step = []
        for number in step:
            next_step.append(one_step(number))
        step = next_step
    return sum(step)


def part2(input_path):
    step = list(map(int, lire_fichier(input_path)))
    monkeys_step = [[step % 10] for step in step]
    for _ in range(2000):
        next_step = []
        for i, number in enumerate(step):
            new_number = one_step(number)
            next_step.append(new_number)
            monkeys_step[i].append(new_number % 10)
        step = next_step
    print("steps computed")
    monkeys_diff = [[sublist[i + 1] - sublist[i] for i in range(len(sublist) - 1)] for sublist in monkeys_step]
    print("diffs computed")
    monkeys_dict = []
    for monkey_step, monkey_diff in zip(monkeys_step, monkeys_diff):
        monkey_dict = {}
        for i in range(len(monkey_diff) - 3):
            if tuple(monkey_diff[i:i + 4]) not in monkey_dict:
                monkey_dict[tuple(monkey_diff[i:i + 4])] = monkey_step[i + 4]
        monkeys_dict.append(monkey_dict)
    print("dict computed")
    diffs_possible = range(-9, 10)
    comb_possible = product(diffs_possible, diffs_possible, diffs_possible, diffs_possible)
    max = 0
    for comb in comb_possible:
        total_comb = 0
        for monkey in monkeys_dict:
            total_comb += monkey.get(comb, 0)
        if total_comb > max:
            max = total_comb
    return max


def one_step(number: int):
    result = number

    temp = result * 64
    result = temp ^ result
    result = result % 16777216

    temp = result // 32
    result = temp ^ result
    result = result % 16777216

    temp = result * 2048
    result = temp ^ result
    result = result % 16777216
    return result
