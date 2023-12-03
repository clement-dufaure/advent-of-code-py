from main.utils.files_utils import lire_fichier


class PartNumber:

    def __init__(self, number: int, num_line: int, min_i: int, max_i: int):
        self.number = number
        self.num_line = num_line
        self.min_i = min_i
        self.max_i = max_i


def est_symbol(caractere: str) -> bool:
    return not caractere.isdigit() and not caractere == "."


def verifier_caracteres_autour(matrice, i, j) -> bool:
    return any(
        0 <= x < len(matrice) and 0 <= y < len(matrice[j]) and est_symbol(matrice[y][x])
        for x in range(i - 1, i + 2)
        for y in range(j - 1, j + 2)
    )


def recuperer_part_numbers(matrice: list[str]) -> list[PartNumber]:
    part_numbers: list[PartNumber] = []
    for j, ligne in enumerate(matrice):
        current_number = ""
        is_part_number = False
        start_index = None
        end_index = None
        for i, caractere in enumerate(ligne):
            if caractere.isdigit():
                if start_index is None:
                    start_index = i
                current_number += caractere
                end_index = i
                if not is_part_number:
                    is_part_number = verifier_caracteres_autour(matrice, i, j)
            elif current_number:
                if is_part_number:
                    part_numbers.append(PartNumber(int(current_number), j, start_index, end_index))
                current_number = ""
                is_part_number = False
                start_index = None
        if current_number and is_part_number:  # part number at the end of line
            part_numbers.append(PartNumber(int(current_number), j, start_index, end_index))
    return part_numbers


def part1(path_input: str) -> int:
    lignes = lire_fichier(path_input)
    part_numbers = recuperer_part_numbers(lignes)
    return sum(part_number.number for part_number in part_numbers)


def get_part_number_arround(i, j, part_numbers) -> list[PartNumber]:
    return [part_number for part_number in part_numbers if
            j - 1 <= part_number.num_line <= j + 1 and i in range(part_number.min_i - 1, part_number.max_i + 2)]


def rechercher_gears(matrice, part_numbers) -> list[int]:
    gears = []
    for j, ligne in enumerate(matrice):
        for i, caractere in enumerate(ligne):
            if caractere == "*":
                arround = get_part_number_arround(i, j, part_numbers)
                if len(arround) == 2:
                    gears.append(arround[0].number * arround[1].number)
    return gears


def part2(path_input: str) -> int:
    lignes = lire_fichier(path_input)
    part_numbers = recuperer_part_numbers(lignes)
    gears = rechercher_gears(lignes, part_numbers)
    return sum(gears)
