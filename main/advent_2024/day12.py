from main.utils.coord_utils import Coord
from main.utils.directions_utils import directions
from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    grid: dict[Coord, str] = {}
    todo: set[Coord] = set()
    for y, ligne in enumerate(lignes):
        for x, lettre in enumerate(ligne):
            grid[Coord(x, y)] = lettre
            todo.add(Coord(x, y))
    score = 0
    while len(todo) > 0:
        zone_en_cours = []
        perimetre_zone = 0
        aire_zone = 1
        first = todo.pop()
        lettre_en_cours = grid[first]
        zone_en_cours.append(first)
        while len(zone_en_cours) > 0:
            to_check = zone_en_cours.pop()
            for direction in ["N", "E", "S", "O"]:
                new_case = to_check + directions[direction]
                # out of grid
                if new_case not in grid.keys():
                    perimetre_zone += 1
                # extend zone ?
                elif new_case not in zone_en_cours:
                    if grid[new_case] == lettre_en_cours:
                        if new_case in todo:
                            todo.remove(new_case)
                            zone_en_cours.append(new_case)
                            aire_zone += 1
                    else:
                        perimetre_zone += 1
        score += perimetre_zone * aire_zone
    return score


class Fence:

    def __init__(self, coord1: Coord, coord2: Coord):
        coord_sorted = sorted([coord1, coord2])
        self.coord1 = coord_sorted[0]
        self.coord2 = coord_sorted[1]

    def __eq__(self, other):
        if isinstance(other, Fence):
            one = sorted([self.coord1, self.coord2])
            two = sorted([other.coord1, other.coord2])
            return self.coord1 == other.coord1 and self.coord2 == other.coord2
        return False

    def __repr__(self):
        coord_sort = sorted([self.coord1, self.coord2])
        return f"{self.coord1}|{self.coord2}"

    def is_in_straight_with(self, other):
        if isinstance(other, Fence):
            one = sorted([self.coord1, self.coord2])
            two = sorted([other.coord1, other.coord2])
            if one[0].x == two[0].x and one[1].x == two[1].x and one[0].y == one[1].y and two[0].y == two[1].y:
                return one[0].y == two[0].y + 1 or one[0].y == two[0].y - 1
            elif one[0].y == two[0].y and one[1].y == two[1].y and one[0].x == one[1].x and two[0].x == two[1].x:
                return one[0].x == two[0].x + 1 or one[0].x == two[0].x - 1
            return False
        raise "error"


def part2(input_path):
    lignes = lire_fichier(input_path)
    grid: dict[Coord, str] = {}
    todo: set[Coord] = set()
    for y, ligne in enumerate(lignes):
        for x, lettre in enumerate(ligne):
            grid[Coord(x, y)] = lettre
            todo.add(Coord(x, y))
    score = 0
    while len(todo) > 0:
        zone_en_cours = []
        perimetre_zone: list[Fence] = []
        aire_zone = 1
        first = todo.pop()
        lettre_en_cours = grid[first]
        zone_en_cours.append(first)
        while len(zone_en_cours) > 0:
            to_check = zone_en_cours.pop()
            for direction in ["N", "E", "S", "O"]:
                new_case = to_check + directions[direction]
                # out of grid
                if new_case not in grid.keys():
                    perimetre_zone.append(Fence(to_check, new_case))
                # extend zone ?
                elif new_case not in zone_en_cours:
                    if grid[new_case] == lettre_en_cours:
                        if new_case in todo:
                            todo.remove(new_case)
                            zone_en_cours.append(new_case)
                            aire_zone += 1
                    else:
                        perimetre_zone.append(Fence(to_check, new_case))
        nb_straights = 0
        perimetre_zone_ini = perimetre_zone
        while len(perimetre_zone) > 0:
            ligne_en_cours = [perimetre_zone.pop()]
            while len(ligne_en_cours) > 0:
                f = ligne_en_cours.pop()
                for fence in perimetre_zone[:]:
                    # case of internal cross
                    if fence.is_in_straight_with(f) and not (
                            Fence(fence.coord1, f.coord1) in perimetre_zone_ini or Fence(fence.coord2,
                                                                                         f.coord2) in perimetre_zone_ini):
                        perimetre_zone.remove(fence)
                        ligne_en_cours.append(fence)
            nb_straights += 1
        score += nb_straights * aire_zone
    return score
