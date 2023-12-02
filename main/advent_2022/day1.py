from main.utils.files_utils import lire_fichier


def part1(path):
    lignes = lire_fichier(path)
    elfs = []
    sum = 0
    for ligne in lignes:
        if ligne != "":
            sum += int(ligne)
        else:
            elfs.append(sum)
            sum = 0
    return max(elfs)


def part2(path):
    lignes = lire_fichier(path)
    elfs = []
    somme = 0
    for ligne in lignes:
        if ligne != "":
            somme += int(ligne)
        else:
            elfs.append(somme)
            somme = 0
    print(elfs)
    elfs = sorted(elfs, reverse=True)[0:3]
    print(elfs)
    return sum(elfs)
