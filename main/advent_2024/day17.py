import re

from main.utils.files_utils import lire_fichier

pattern = r"Register A: (\d+)Register B: (\d+)Register C: (\d+)Program: ([,\d]+)"


class Machine:

    def __init__(self, A: int, B: int, C: int, program: list[int]):
        self.A = A
        self.B = B
        self.C = C
        self.program = program
        self.index = 0
        self.output = []

    def run(self, stop_at_first_output=False):
        while self.index < len(self.program):
            if self.program[self.index] == 0:
                self.adv(self.program[self.index + 1])
                continue
            if self.program[self.index] == 1:
                self.bxl(self.program[self.index + 1])
                continue
            if self.program[self.index] == 2:
                self.bst(self.program[self.index + 1])
                continue
            if self.program[self.index] == 3:
                self.jnz(self.program[self.index + 1])
                continue
            if self.program[self.index] == 4:
                self.bxc(self.program[self.index + 1])
                continue
            if self.program[self.index] == 5:
                self.out(self.program[self.index + 1])
                if stop_at_first_output:
                    break
                continue
            if self.program[self.index] == 6:
                self.bdv(self.program[self.index + 1])
                continue
            if self.program[self.index] == 7:
                self.cdv(self.program[self.index + 1])
                continue

    def combo(self, operande: int):
        if 0 <= operande <= 3:
            return operande
        if operande == 4:
            return self.A
        if operande == 5:
            return self.B
        if operande == 6:
            return self.C
        else:
            raise "Invalid program"

    def adv(self, operande: int):
        self.A = int(self.A / pow(2, self.combo(operande)))
        self.index += 2

    def bxl(self, operande):
        self.B = self.B ^ operande
        self.index += 2

    def bst(self, operande):
        self.B = self.combo(operande) % 8
        self.index += 2

    def jnz(self, operande):
        if not self.A == 0:
            self.index = operande
        else:
            self.index += 2

    def bxc(self, operande):
        self.B = self.B ^ self.C
        self.index += 2

    def out(self, operande):
        self.output.append(self.combo(operande) % 8)
        self.index += 2

    def bdv(self, operande):
        self.B = int(self.A / pow(2, self.combo(operande)))
        self.index += 2

    def cdv(self, operande):
        self.C = int(self.A / pow(2, self.combo(operande)))
        self.index += 2


def part1(input_path):
    lignes = lire_fichier(input_path)
    read = re.search(pattern, "".join(lignes))
    machine = Machine(int(read.group(1)), int(read.group(2)), int(read.group(3)),
                      list(map(int, read.group(4).split(","))))
    machine.run()
    return ",".join(list(map(str, machine.output)))


# Programme fourni = A chaque etape,
# output d'une valeur dépendant uniquement de a (partie de l'algo variable de l'input)
# division entiere de a par 8
# si a=0 : stop
# pour chaque valeur possible d'une étape donnée (la première est 0 correspondant à l'arret du programme)
# recherche de la valeur output suivante (premiere sortie de la machine)
# qui doit donc etre obtenue par un nouveau a
# compris entre a*8 et (a+1)*8 pour arriver à la valeur courante a par division entiere par 8
def recursif(a: int, program_restant: list[int], program_initial: list[int]):
    for new_a in range(a * 8, (a + 1) * 8):
        if compute(new_a, program_initial) == program_restant[-1]:
            if len(program_restant) == 1:
                return new_a
            else:
                check = recursif(new_a, program_restant[:-1], program_initial)
                if check != -1:
                    return check
    return -1  # pas de correspondance


def compute(a: int, program: list[int]):
    machine = Machine(a, 0, 0, program)
    machine.run(stop_at_first_output=True)
    return machine.output[0]


def part2(input_path):
    lignes = lire_fichier(input_path)
    read = re.search(pattern, "".join(lignes))
    program = list(map(int, read.group(4).split(",")))
    return recursif(0, program, program)
