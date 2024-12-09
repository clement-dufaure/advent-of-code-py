from main.utils.files_utils import lire_fichier


class File:
    def __init__(self, id: int, size: int, start: int):
        self.id = id
        self.size = size
        self.start = start

    def __repr__(self):
        return f"{self.id} : {self.start} -> {self.start + self.size - 1}"


class Space:
    def __init__(self, size: int, start: int):
        self.size = size
        self.start = start

    def __repr__(self):
        return f"{self.start} -> {self.start + self.size - 1}"


def part1(input_path):
    lignes = lire_fichier(input_path)
    read_file = True
    current_id = 0
    disk: list[int] = []
    for chiffre in lignes[0]:
        if read_file:
            disk = disk + [current_id] * int(chiffre)
            current_id += 1
        else:
            disk = disk + [-1] * int(chiffre)
        read_file = not read_file
    pos = 0
    while pos < len(disk):
        if disk[pos] == -1:
            disk[pos] = disk.pop()
        pos += 1
        # clean
        while disk[len(disk) - 1] == -1:
            disk.pop()
    checksum = 0
    for i, id in enumerate(disk):
        checksum += i * id
    return checksum


def part2(input_path):
    lignes = lire_fichier(input_path)
    read_file = True
    current_id = 0
    files: list[File] = []
    spaces: list[Space] = []
    current_pos = 0
    for chiffre in lignes[0]:
        if read_file:
            files.append(File(current_id, int(chiffre), current_pos))
            current_id += 1
        else:
            if int(chiffre) > 0:
                spaces.append(Space(int(chiffre), current_pos))
        read_file = not read_file
        current_pos += int(chiffre)
    new_spaces = []
    for file in reversed(files):
        for space in spaces:
            if space.start > file.start:
                break
            if file.size <= space.size:
                new_spaces.append(Space(file.size, file.start))
                file.start = space.start
                if file.size == space.size:
                    spaces.remove(space)
                else:
                    space.start += file.size
                    space.size -= file.size
                break
    files = sorted(files, key=lambda my_file: my_file.start)
    spaces = sorted(spaces + new_spaces, key=lambda my_space: my_space.start)
    pos = 0
    next_file = 0
    next_space = 0
    checksum = 0
    while True:
        if next_file >= len(files) and next_space >= len(spaces):
            break
        if next_file < len(files) and files[next_file].start == pos:
            for _ in range(files[next_file].size):
                checksum += pos * files[next_file].id
                pos += 1
            next_file += 1
        elif next_space < len(spaces) and spaces[next_space].start == pos:
            pos += spaces[next_space].size
            next_space += 1
        else:
            raise "pas normal"
    return checksum
