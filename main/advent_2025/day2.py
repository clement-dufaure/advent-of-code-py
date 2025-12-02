from main.utils.files_utils import lire_fichier


def part1(input_path):
    ligne = lire_fichier(input_path)[0]
    invalid_ids = []
    ranges = ligne.split(",")
    for one_range in ranges:
        [start, end] = one_range.split("-")
        one_numerical_range = range(int(start), int(end) + 1)
        for i in one_numerical_range:
            str_i = str(i)
            if len(str_i) % 2 == 0:
                half = int(len(str_i) / 2)
                part_1 = str_i[:half]
                part_2 = str_i[half:]
                if part_1 == part_2:
                    invalid_ids.append(i)
    return sum(invalid_ids)


def part2(input_path):
    ligne = lire_fichier(input_path)[0]
    invalid_ids = []
    ranges = ligne.split(",")
    for one_range in ranges:
        [start, end] = one_range.split("-")
        one_numerical_range = range(int(start), int(end) + 1)
        for i in one_numerical_range:
            if is_recurrent_str(str(i)):
                invalid_ids.append(i)
    return sum(invalid_ids)


def is_recurrent_str(my_str):
    for i in range(1, len(my_str)):
        test = my_str[0:i]
        j = i
        ok = True
        while j < len(my_str):
            if my_str[j:j + i] != test:
                ok = False
                break
            j = j + i
        if ok:
            return True
    return False
