from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    count = 50
    password = 0
    for ligne in lignes:
        direction = ligne[0]
        distance = int(ligne[1:])
        if direction == "L":
            count = (count - distance) % 100
        if direction == "R":
            count = (count + distance) % 100
        if count == 0:
            password += 1
    return password


def part2(input_path):
    lignes = lire_fichier(input_path)
    count = 50
    password = 0
    for ligne in lignes:
        direction = ligne[0]
        distance = int(ligne[1:])
        password += int(distance / 100)
        distance_ajustee = distance % 100
        new_count_absolute = 0
        if direction == "L":
            new_count_absolute = count - distance_ajustee
        if direction == "R":
            new_count_absolute = count + distance_ajustee
        if (count != 0 and new_count_absolute < 0) or new_count_absolute > 100:
            password += 1
        count = new_count_absolute % 100
        if count == 0:
            password += 1
    return password
