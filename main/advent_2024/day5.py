from functools import cmp_to_key

from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    rules = []
    books = []
    for ligne in lignes:
        if "|" in ligne:
            rule = ligne.split("|")
            rules.append(rule)
        if "," in ligne:
            books.append(ligne.split(","))
    somme = 0
    for book in books:
        ok = True
        for rule in rules:
            if rule[0] in book and rule[1] in book and not book.index(rule[0]) < book.index(rule[1]):
                ok = False
                break
        if ok:
            somme += int(book[len(book) // 2])
    return somme


def part2(input_path):
    lignes = lire_fichier(input_path)
    rules = []
    books = []
    for ligne in lignes:
        if "|" in ligne:
            rule = ligne.split("|")
            rules.append(rule)
        if "," in ligne:
            books.append(ligne.split(","))
    compare = get_fct_compare(rules)
    somme = 0
    for book in books:
        ok = True
        for rule in rules:
            if rule[0] in book and rule[1] in book and not book.index(rule[0]) < book.index(rule[1]):
                ok = False
                break
        if not ok:
            book = sorted(book, key=cmp_to_key(compare))
            somme += int(book[len(book) // 2])
    return somme


def get_fct_compare(rules):
    def compare(a, b):
        for rule in rules:
            if a == rule[0] and b == rule[1]:
                return -1
            if a == rule[1] and b == rule[0]:
                return 1
    return compare
