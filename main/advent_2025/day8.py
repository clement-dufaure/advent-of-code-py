from math import prod

from numpy import unravel_index, fill_diagonal, inf, tril_indices
from numpy.ma.core import argmin
from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import pdist, squareform

from main.utils.files_utils import lire_fichier


def part1(input_path, nb_iterations):
    lignes = lire_fichier(input_path)
    boxes = []
    for ligne in lignes:
        boxes.append([int(point) for point in ligne.split(",")])
    distances = squareform(pdist(boxes))
    lower_triangle = tril_indices(len(lignes))
    distances[lower_triangle] = inf
    classes = [[i] for i in range(len(lignes))]
    for _ in range(nb_iterations):
        index_distance_mini = argmin(distances)
        coord_distance_mini = unravel_index(index_distance_mini, distances.shape)
        distances[coord_distance_mini] = inf
        x = coord_distance_mini[0]
        y = coord_distance_mini[1]
        classe1 = []
        classe2 = []
        new_classes = []
        for classe in classes:
            if x in classe:
                classe1 = classe
            elif y in classe:
                classe2 = classe
            else:
                new_classes.append(classe)
        new_classes.append(classe1 + classe2)
        classes = new_classes
    classes_by_len = sorted(classes, key=lambda c: len(c), reverse=True)
    return prod([len(c) for c in classes_by_len[:3]])


def part2(input_path):
    lignes = lire_fichier(input_path)
    boxes = []
    for ligne in lignes:
        boxes.append([int(point) for point in ligne.split(",")])
    distances = squareform(pdist(boxes))
    lower_triangle = tril_indices(len(lignes))
    distances[lower_triangle] = inf
    classes = [[i] for i in range(len(lignes))]
    while len(classes) > 1:
        index_distance_mini = argmin(distances)
        coord_distance_mini = unravel_index(index_distance_mini, distances.shape)
        distances[coord_distance_mini] = inf
        x = coord_distance_mini[0]
        y = coord_distance_mini[1]
        classe1 = []
        classe2 = []
        new_classes = []
        for classe in classes:
            if x in classe:
                classe1 = classe
            elif y in classe:
                classe2 = classe
            else:
                new_classes.append(classe)
        new_classes.append(classe1 + classe2)
        classes = new_classes
    return int(lignes[coord_distance_mini[0]].split(",")[0]) * int(lignes[coord_distance_mini[1]].split(",")[0])
