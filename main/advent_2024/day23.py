import itertools

from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    lans = {}
    for ligne in lignes:
        pcs = ligne.split("-")
        if pcs[0] not in lans:
            lans[pcs[0]] = set()
        if pcs[1] not in lans:
            lans[pcs[1]] = set()
        lans[pcs[0]].add(pcs[1])
        lans[pcs[1]].add(pcs[0])
    sets_ok = set()
    for pc in lans:
        if pc.startswith("t"):
            for other_pc in lans[pc]:
                for other_other_pc in lans[other_pc]:
                    if other_other_pc != pc and pc in lans[other_other_pc]:
                        tuple_trie = tuple(sorted([pc, other_pc, other_other_pc]))
                        sets_ok.add(tuple_trie)
    return len(sets_ok)


def part2(input_path):
    lignes = lire_fichier(input_path)
    lans = {}
    for ligne in lignes:
        pcs = ligne.split("-")
        if pcs[0] not in lans:
            lans[pcs[0]] = set()
        if pcs[1] not in lans:
            lans[pcs[1]] = set()
        lans[pcs[0]].add(pcs[1])
        lans[pcs[1]].add(pcs[0])
    max_set = set()
    for p, pc in enumerate(lans):
        print(f"{p} of {len(lans)}")
        subsets = []
        for r in range(1, len(lans[pc]) + 2):
            subsets.extend(itertools.combinations({pc} | lans[pc], r))
        for subset in subsets:
            ok = True
            for i in subset:
                if ok:
                    for j in subset:
                        if i != j:
                            if i not in lans[j]:
                                ok = False
                                break
            if ok:
                if len(subset) > len(max_set):
                    max_set = subset
    return ",".join(sorted(list(max_set)))
