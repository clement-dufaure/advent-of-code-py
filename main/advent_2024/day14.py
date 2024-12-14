import re

from main.utils.coord_utils import Coord
from main.utils.files_utils import lire_fichier

pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"


class Robot:

    def __init__(self, sx: int, sy: int, vx: int, vy: int):
        self.sx = sx
        self.sy = sy
        self.vx = vx
        self.vy = vy


def part1(input_path, max_x=11, max_y=7):
    lignes = lire_fichier(input_path)
    robots: list[Robot] = []
    for result in re.findall(pattern, "".join(lignes)):
        robots.append(Robot(int(result[0]), int(result[1]), int(result[2]), int(result[3])))
    pos_after_100: list[Coord] = []
    for robot in robots:
        fx = (robot.sx + 100 * robot.vx) % max_x
        fy = (robot.sy + 100 * robot.vy) % max_y
        pos_after_100.append(Coord(fx, fy))
    mid_x = max_x // 2
    mid_y = max_y // 2
    nb_qno, nb_qne, nb_qso, nb_qse = 0, 0, 0, 0
    for coord in pos_after_100:
        if coord.x == mid_x or coord.y == mid_y:
            continue
        if coord.x < mid_x and coord.y < mid_y:
            nb_qno += 1
        elif coord.x > mid_x and coord.y < mid_y:
            nb_qne += 1
        elif coord.x < mid_x and coord.y > mid_y:
            nb_qso += 1
        elif coord.x > mid_x and coord.y > mid_y:
            nb_qse += 1
    return nb_qno * nb_qne * nb_qso * nb_qse


def part2(input_path, max_x=11, max_y=7):
    lignes = lire_fichier(input_path)
    robots: list[Robot] = []
    for result in re.findall(pattern, "".join(lignes)):
        robots.append(Robot(int(result[0]), int(result[1]), int(result[2]), int(result[3])))
    # tassement horizontaux
    #    i = 12
    #    while True:
    #        print(f"i={i}")
    #        coord_robots = []
    #        for robot in robots:
    #            coord_robots.append(Coord((robot.sx + i * robot.vx) % max_x, (robot.sy + i * robot.vy) % max_y))
    #        draw_grid(coord_robots, max_x, max_y)
    #        i += 101
    # tassement verticaux
    #    i = 88
    #    while True:
    #        print(f"i={i}")
    #        coord_robots = []
    #        for robot in robots:
    #            coord_robots.append(Coord((robot.sx + i * robot.vx) % max_x, (robot.sy + i * robot.vy) % max_y))
    #        draw_grid(coord_robots, max_x, max_y)
    #        i += 103
    # ppmc
    i = 6577
    coord_robots = []
    for robot in robots:
        coord_robots.append(Coord((robot.sx + i * robot.vx) % max_x, (robot.sy + i * robot.vy) % max_y))
    draw_grid(coord_robots, max_x, max_y)


def draw_grid(coord_robots, max_x, max_y):
    out = ""
    for y in range(max_y):
        for x in range(max_x):
            if Coord(x, y) in coord_robots:
                out += "# "
            else:
                out += "  "
        out += "\n"
    print(out)
