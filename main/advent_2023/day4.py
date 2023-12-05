import re

from main.utils.files_utils import lire_fichier


def number_of_win(scratchcard: str) -> int:
    _, data = scratchcard.split(":")
    winning, my_numbers = data.split("|")
    winning_list = re.findall(r"(\d+)", winning)
    my_numbers_list = re.findall(r"(\d+)", my_numbers)
    return len([number for number in my_numbers_list if number in winning_list])


def part1(input_path):
    total = 0
    for scratchcard in lire_fichier(input_path):
        wins = number_of_win(scratchcard)
        total += 2 ** (wins - 1) if wins > 0 else 0
    return total


def part2(input_path):
    scratchcards = lire_fichier(input_path)
    number_scratchcard = [1] * len(scratchcards)
    for current_id, current_scratchcard in enumerate(scratchcards):
        wins = number_of_win(current_scratchcard)
        for i in range(current_id + 1, current_id + 1 + wins):
            number_scratchcard[i] += number_scratchcard[current_id]
    return sum(number_scratchcard)
