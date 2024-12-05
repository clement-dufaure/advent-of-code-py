from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    list1: list[int] = []
    list2: list[int] = []
    for ligne in lignes:
        pair = ligne.split("   ")
        list1.append(int(pair[0]))
        list2.append(int(pair[1]))
    list1 = sorted(list1)
    list2 = sorted(list2)
    somme = 0
    for item1, item2 in zip(list1, list2):
        somme += abs(item1 - item2)
    return somme


def part2(input_path):
    lignes = lire_fichier(input_path)
    list1: list[int] = []
    list2: list[int] = []
    for ligne in lignes:
        pair = ligne.split("   ")
        list1.append(int(pair[0]))
        list2.append(int(pair[1]))
    somme = 0
    for item in list1:
        somme += item * list2.count(item)
    return somme
