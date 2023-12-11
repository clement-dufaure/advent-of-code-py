from main.utils.coord_utils import Coord


def connected_points(max_x: int, max_y: int, start: Coord, obstacles: list[Coord]):
    connected = set()
    queue = [start]
    while queue:
        current = queue.pop(0)
        connected.add(current)
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor = Coord(current.x + i, current.y + j)
                if (
                        0 <= neighbor.x < max_x and
                        0 <= neighbor.y < max_y and
                        neighbor not in obstacles and
                        neighbor not in connected and
                        neighbor not in queue
                ):
                    queue.append(neighbor)
    return connected
