import re

from main.utils.files_utils import lire_fichier

regex_wire = r"([a-z0-9]+): (\d)"
regex_gate = r"([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)"


def part1(input_path):
    lignes = lire_fichier(input_path)
    wires = {}
    wires_z = []
    gates = set()
    for match_wire in re.findall(regex_wire, " ".join(lignes)):
        wires[match_wire[0]] = True if match_wire[1] == "1" else False
        if match_wire[0][0] == "z":
            wires_z.append(match_wire[0])
    for match_gate in re.findall(regex_gate, " ".join(lignes)):
        gates.add((match_gate[0], match_gate[1], match_gate[2], match_gate[3]))
        if match_gate[3][0] == "z":
            wires_z.append(match_gate[3])
    binary_str = execute(gates, wires, wires_z)
    return int(binary_str, 2)


def part2(input_path):
    lignes = lire_fichier(input_path)
    wires = {}
    wires_x = []
    wires_y = []
    wires_z = []
    gates = set()
    for match_wire in re.findall(regex_wire, " ".join(lignes)):
        wires[match_wire[0]] = True if match_wire[1] == "1" else False
        if match_wire[0][0] == "x":
            wires_x.append(match_wire[0])
        if match_wire[0][0] == "y":
            wires_y.append(match_wire[0])
    for match_gate in re.findall(regex_gate, " ".join(lignes)):
        op1 = match_gate[0]
        op2 = match_gate[2]
        s = sorted([op1, op2])
        gates.add((s[0], match_gate[1], s[1], match_gate[3]))
        if match_gate[3][0] == "z":
            wires_z.append(match_gate[3])

    # errors
    # nbc : y05 XOR x05 -> nbc
    # svm : y05 AND x05 -> svm
    gates.remove(("x05", "AND", "y05", "svm"))
    gates.remove(("x05", "XOR", "y05", "nbc"))
    gates.add(("x05", "AND", "y05", "nbc"))
    gates.add(("x05", "XOR", "y05", "svm"))

    # dkk OR pbd -> z15
    # fwr XOR cpv -> kqk
    gates.remove(("dkk", "OR", "pbd", "z15"))
    gates.remove(("cpv", "XOR", "fwr", "kqk"))
    gates.add(("dkk", "OR", "pbd", "kqk"))
    gates.add(("cpv", "XOR", "fwr", "z15"))

    # x23 AND y23 -> z23
    # kph XOR hpw -> cgq
    gates.remove(("x23", "AND", "y23", "z23"))
    gates.remove(("hpw", "XOR", "kph", "cgq"))
    gates.add(("x23", "AND", "y23", "cgq"))
    gates.add(("hpw", "XOR", "kph", "z23"))

    # bdr XOR fsp -> fnr
    # fsp AND bdr -> z39
    gates.remove(("bdr", "XOR", "fsp", "fnr"))
    gates.remove(("bdr", "AND", "fsp", "z39"))
    gates.add(("bdr", "XOR", "fsp", "z39"))
    gates.add(("bdr", "AND", "fsp", "fnr"))

    execute(gates, wires, wires_z)

    errors = sorted(["svm", "nbc", "z15", "kqk", "z23", "cgq", "fnr", "z39"])
    return ",".join(errors)


vrais_calculs = {}


def get_vrais_calculs():
    if len(vrais_calculs) > 0:
        return vrais_calculs
    retenue = ""
    for i in range(46):
        i_formate = "{:02d}".format(i)
        value = "(x" + i_formate + "XOR" + "y" + i_formate + ")"
        if i == 1:
            value = "(" + retenue + "XOR" + value + ")"
        elif retenue != "":
            value = "((" + retenue + ")XOR" + value + ")"
        vrais_calculs["z" + i_formate] = value
        possibilite_retenue_1 = "(x" + i_formate + "AND" + "y" + i_formate + ")"
        if retenue == "":
            retenue = possibilite_retenue_1
        else:
            if i > 1:
                possibilite_retenue2 = "(" + retenue + ")" + "AND" + "(x" + i_formate + "XOR" + "y" + i_formate + ")"
            else:
                possibilite_retenue2 = retenue + "AND" + "(x" + i_formate + "XOR" + "y" + i_formate + ")"
            retenue = "(" + possibilite_retenue2 + ")" + "OR" + possibilite_retenue_1
    return vrais_calculs


def execute(gates, wires, wires_z):
    vrais_calculs = get_vrais_calculs()
    tous_les_z = False
    update_wires = {}
    wire_en_clair = {}
    calculs_reels = {}
    while not tous_les_z:
        for gate in gates:
            # on ne retouche pas a une sortie deja traitee
            if gate[3] not in wires:
                if gate[0] in wires and gate[2] in wires:
                    update_wires[gate[3]] = operation(wires[gate[0]], gate[1], wires[gate[2]])
                    rewrite_op1 = wire_en_clair.get(gate[0], gate[0])
                    rewrite_op2 = wire_en_clair.get(gate[2], gate[2])
                    s = sorted([rewrite_op1, rewrite_op2])
                    if not gate[3][0] == "z":
                        rewrite_result = ('(' + s[0]
                                          + gate[1]
                                          + s[1] + ')')
                        wire_en_clair[gate[3]] = rewrite_result
                    else:
                        calculs_reels[gate[3]] = ('(' + s[0]
                                                  + gate[1]
                                                  + s[1] + ')')
        wires.update(update_wires)
        update_wires = {}
        ok = True
        for wire_z in wires_z:
            if wire_z not in wires:
                ok = False
                break
        tous_les_z = ok

    reverted_wires_en_clair = {v: k for k, v in wire_en_clair.items()}
    for i in range(46):
        theorie = vrais_calculs["z" + "{:02d}".format(i)]
        pratique = calculs_reels["z" + "{:02d}".format(i)]
        if not theorie == pratique:
            print(theorie)
            print(pratique)
            print(f"error at {"z" + "{:02d}".format(i)}")

    binary_str = ""
    wires_z = sorted(wires_z, reverse=True)
    for wire_z in wires_z:
        binary_str += "1" if wires[wire_z] else "0"
    return binary_str


def operation(op1, operator, op2):
    if operator == "AND":
        return op1 and op2
    if operator == "OR":
        return op1 or op2
    else:
        return op1 != op2
