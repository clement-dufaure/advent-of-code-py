from main.utils.files_utils import lire_fichier

digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def part1(input_path):
    lignes = lire_fichier(input_path)
    somme = 0
    for ligne in lignes:
        chiffres = []
        for char in ligne:
            if char.isdigit():
                chiffres.append(char)
        calibre = chiffres[0] + chiffres[-1]
        somme += int(calibre)
    return somme


def part2(input_path):
    lignes = lire_fichier(input_path)
    somme = 0
    for ligne in lignes:
        chiffres = []
        for i in range(len(ligne)):
            if ligne[i].isdigit():
                chiffres.append(ligne[i])
            else:
                for j in range(len(digits)):
                    if ligne[i:].startswith(digits[j]):
                        chiffres.append(str(j))
                        break
        calibre = chiffres[0] + chiffres[-1]
        somme += int(calibre)
    return somme
