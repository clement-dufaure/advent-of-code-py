from main.utils.files_utils import lire_fichier


def part1(input_path):
    lignes = lire_fichier(input_path)
    stones = list(map(int, lignes[0].split(" ")))
    for _ in range(25):
        stones = boucle(stones)
    return len(stones)


def boucle(stones: list[int]):
    new_stones: list[int] = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.append(int(str(stone)[0:len(str(stone)) // 2]))
            new_stones.append(int(str(stone)[len(str(stone)) // 2:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones


memoire: dict[tuple[int, int], int] = {}


def recursif(stone: int, iteration: int, max_iteration: int):
    key = (stone, iteration)
    if key in memoire:
        return memoire[key]
    finish = iteration == max_iteration
    if stone == 0:
        result = 1 if finish else recursif(1, iteration + 1, max_iteration)
    elif len(str(stone)) % 2 == 0:
        if finish:
            result = 2
        else:
            stone1 = int(str(stone)[0:len(str(stone)) // 2])
            stone2 = int(str(stone)[len(str(stone)) // 2:])
            result = recursif(stone1, iteration + 1, max_iteration) + recursif(stone2, iteration + 1, max_iteration)
    else:
        result = 1 if finish else recursif(stone * 2024, iteration + 1, max_iteration)
    memoire[key] = result
    return result


def part2(input_path):
    lignes = lire_fichier(input_path)
    stones = list(map(int, lignes[0].split(" ")))
    total = 0
    for i, stone in enumerate(stones):
        total += recursif(stone, 0, 74)
    return total
