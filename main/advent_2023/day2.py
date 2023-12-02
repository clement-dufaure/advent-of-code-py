import re

from main.utils.files_utils import lire_fichier

pattern_tirage = r"(\d+) (\w+)"


def read_input(input_path):
    lignes = lire_fichier(input_path)
    games = {}
    for ligne in lignes:
        identifiant, sets_str = ligne.split(":")
        sets = []
        for set_str in sets_str.split(";"):
            set = {}
            for resultat in re.findall(pattern_tirage, set_str):
                nombre, couleur = resultat
                set[couleur] = int(nombre)
            sets.append(set)
        games[int(identifiant.split(" ")[1])] = sets
    return games


def check_game_ok(sets: list[dict[str, int]]) -> bool:
    for set in sets:
        if set.get("red", 0) > 12 or set.get("green", 0) > 13 or set.get("blue", 0) > 14:
            return False
    return True


def part1(input_path) -> int:
    games = read_input(input_path)
    games_ok = {identifiant: sets for identifiant, sets in games.items() if check_game_ok(sets)}
    return sum(games_ok.keys())


def power_game(sets: list[dict[str, int]]) -> int:
    max_red = max([set.get("red", 0) for set in sets])
    max_green = max([set.get("green", 0) for set in sets])
    max_blue = max([set.get("blue", 0) for set in sets])
    return max_red * max_green * max_blue


def part2(input_path) -> int:
    games = read_input(input_path)
    return sum(map(power_game, games.values()))
