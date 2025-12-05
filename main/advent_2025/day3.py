from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    joltages = [int(max_under_constraint(ligne, 2)) for ligne in lignes]
    return sum(joltages)


def part2(input_path):
    lignes = lire_fichier(input_path)
    joltages = [int(max_under_constraint(ligne, 12)) for ligne in lignes]
    return sum(joltages)


def max_under_constraint(chaine, remaining_size):
    max_digit = max(chaine[:len(chaine) - (remaining_size - 1)])
    if remaining_size == 1:
        return max_digit
    else:
        index_max = chaine.index(max_digit)
        return max_digit + max_under_constraint(chaine[index_max + 1:], remaining_size - 1)
