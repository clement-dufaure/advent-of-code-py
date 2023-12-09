import re

from main.utils.files_utils import lire_fichier
from main.utils.math_utils import ppmc_de_liste


def part1(inputh_path):
    lignes = lire_fichier(inputh_path)
    instructions = lignes[0]
    network: dict[str, tuple[str, str]] = {}
    for ligne in lignes[2:]:
        src, left, right = re.findall(r"([A-Z]+)", ligne)
        network[src] = (left, right)
    point = "AAA"
    nombre_etapes = 0
    while point != "ZZZ":
        instruction_int = 0 if instructions[nombre_etapes % len(instructions)] == "L" else 1
        nombre_etapes += 1
        point = network.get(point)[instruction_int]
    return nombre_etapes


def part2(inputh_path):
    lignes = lire_fichier(inputh_path)
    instructions = lignes[0]
    network: dict[str, tuple[str, str]] = {}
    for ligne in lignes[2:]:
        src, left, right = re.findall(r"([0-9A-Z]+)", ligne)
        network[src] = (left, right)
    points = [key for key in network.keys() if key[2] == "A"]
    # On admet que la taille du premier chemin A->Z et des suivants Z->Z sont de même taille
    taille_boucle_points = []
    for point in points:
        nombre_etapes = 0
        while point[2] != "Z":
            instruction_int = 0 if instructions[nombre_etapes % len(instructions)] == "L" else 1
            point = network.get(point)[instruction_int]
            nombre_etapes += 1
        taille_boucle_points.append(nombre_etapes)
    return ppmc_de_liste(taille_boucle_points)
