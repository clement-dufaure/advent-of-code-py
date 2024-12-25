from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    towels = lignes[0].split(", ")
    patterns = lignes[2:]
    nb_possible = 0
    for i, pattern in enumerate(patterns):
        print(f"{i} of {len(patterns)}")
        if is_pattern_possible(pattern, towels):
            nb_possible += 1
    return nb_possible


def is_pattern_possible(pattern, towels):
    builds = {""}
    while len(builds) > 0:
        new_builds = set()
        for build in builds:
            for towel in towels:
                if build + towel == pattern:
                    return True
                if pattern.startswith(towel, len(build)):
                    new_builds.add(build + towel)
        builds = new_builds
    return False


def how_many_pattern_possible(pattern, towels):
    builds = {"": 1}
    nb = 0
    while len(builds) > 0:
        new_builds = {}
        for build in builds.items():
            for towel in towels:
                check = build[0] + towel
                if check == pattern:
                    nb += build[1]
                if pattern.startswith(towel, len(build[0])):
                    new_builds[check] = new_builds.get(check, 0) + build[1]
        builds = new_builds
    return nb


def part2(input_path):
    lignes = lire_fichier(input_path)
    towels = lignes[0].split(", ")
    patterns = lignes[2:]
    total = 0
    for i, pattern in enumerate(patterns):
        print(f"{i} of {len(patterns)}")
        total += how_many_pattern_possible(pattern, towels)
    return total
