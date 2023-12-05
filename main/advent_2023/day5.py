import re

from main.utils.files_utils import lire_fichier


def part1(input_path) -> int:
    lignes = lire_fichier(input_path)
    seeds: list[int] = list(map(int, re.findall(r"\d+", lignes[0])))
    mapped: list[bool] = [False] * len(seeds)
    index_ligne = 3
    while index_ligne < len(lignes):
        if lignes[index_ligne] != "":
            destination_range_start, source_range_start, length = list(
                map(int, re.findall(r"\d+", lignes[index_ligne])))
            for index_seed, seed in enumerate(seeds):
                if not mapped[index_seed] and seed in range(source_range_start, source_range_start + length):
                    mapped[index_seed] = True
                    seeds[index_seed] = destination_range_start + (seed - source_range_start)
            index_ligne += 1
        else:
            mapped = [False] * len(seeds)
            index_ligne += 2
    return min(seeds)


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"({self.start}, {self.end})"


class SeedMapping:
    def __init__(self, source_start: int, destination_start: int, length: int):
        self.source_start = source_start
        self.destination_start = destination_start
        self.length = length
        self.source_end = source_start + length
        self.destination_end = destination_start + length

    def __repr__(self):
        return f"({self.source_start}, {self.source_end} -> {self.destination_start}, {self.destination_end})"


def recuperer_intervalles(nombres: list[int]) -> list[Interval]:
    intervalles = []
    for i in range(0, len(nombres), 2):
        debut_intervalle = nombres[i]
        taille = nombres[i + 1]
        fin_intervalle = debut_intervalle + taille
        intervalles.append(Interval(debut_intervalle, fin_intervalle))
    return intervalles


def mettre_a_jour_intervalles(intervalles: list[Interval], mappings: list[SeedMapping]) -> list[Interval]:
    intervalles_non_mis_a_jour = intervalles
    intervalles_mis_a_jour = []
    for seedMapping in mappings:
        intervalles_temp = intervalles_non_mis_a_jour
        intervalles_non_mis_a_jour = []
        for intervalle in intervalles_temp:
            if seedMapping.source_end < intervalle.start or intervalle.end < seedMapping.source_start:
                # disjoint : No matching, no change
                intervalles_non_mis_a_jour.append(intervalle)
            else:
                if intervalle.start <= seedMapping.source_start and seedMapping.source_end <= intervalle.end:
                    # match inclu dans intervalle
                    if intervalle.start != seedMapping.source_start:
                        intervalles_non_mis_a_jour.append(Interval(intervalle.start, seedMapping.source_start - 1))
                    intervalles_mis_a_jour.append(Interval(seedMapping.destination_start, seedMapping.destination_end))
                    if intervalle.end != seedMapping.source_end:
                        intervalles_non_mis_a_jour.append(Interval(seedMapping.source_end + 1, intervalle.end))
                elif seedMapping.source_start <= intervalle.start and intervalle.end <= seedMapping.source_end:
                    # intervalle inclu dans match
                    dest_real_start = seedMapping.destination_start + (intervalle.start - seedMapping.source_start)
                    dest_real_end = seedMapping.destination_end - (seedMapping.source_end - intervalle.end)
                    intervalles_mis_a_jour.append(Interval(dest_real_start, dest_real_end))
                elif seedMapping.source_start <= intervalle.start and seedMapping.source_end <= intervalle.end:
                    dest_real_start = seedMapping.destination_start + (intervalle.start - seedMapping.source_start)
                    intervalles_mis_a_jour.append(Interval(dest_real_start, seedMapping.destination_end))
                    intervalles_non_mis_a_jour.append(Interval(seedMapping.source_end, intervalle.end))
                elif intervalle.start <= seedMapping.source_start and intervalle.end <= seedMapping.source_end:
                    intervalles_non_mis_a_jour.append(Interval(intervalle.start, seedMapping.source_start))
                    dest_real_end = seedMapping.destination_end - (seedMapping.source_end - intervalle.end)
                    intervalles_mis_a_jour.append(Interval(seedMapping.destination_start, dest_real_end))
    return intervalles_mis_a_jour + intervalles_non_mis_a_jour


def part2(input_path) -> int:
    lignes = lire_fichier(input_path)
    seed_ranges = recuperer_intervalles(list(map(int, re.findall(r"\d+", lignes[0]))))
    index_ligne = 3
    mappings: list[SeedMapping] = []
    while index_ligne < len(lignes):
        if lignes[index_ligne] != "":
            destination_range_start, source_range_start, length = list(
                map(int, re.findall(r"\d+", lignes[index_ligne])))
            mappings.append(SeedMapping(source_range_start, destination_range_start, length))
            index_ligne += 1
        else:
            seed_ranges = mettre_a_jour_intervalles(seed_ranges, mappings)
            mappings = []
            index_ligne += 2
    return min(seed_ranges, key=lambda obj: obj.start).start
