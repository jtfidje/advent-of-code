import math
import json
from collections import defaultdict
from functools import reduce
from typing import Any

def json_print(obj: dict | list) -> None:
    print(json.dumps(obj, indent=4))


def read_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        for i, line in enumerate(lines):
            segments = line.split(" -> ")
            for j, segment in enumerate(segments):
                segments[j] = list(map(int, segment.split(",")))
            lines[i] = segments

        return lines


def read_numbers(path: str) -> list[int]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return list(map(int, lines))


def solve_1(path: str) -> Any:
    data = read_lines(path)
    min_x, min_y = math.inf, math.inf
    max_x, max_y = 0, 0
    for line in data:

        for (x, y) in line:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

    _map = [["."] * (max_x - min_x + 1) for _ in range(max_y + 1)]

    for line in data:
        for i, segments in enumerate(line[1:], start=1):
            x_1, y_1 = line[i - 1]
            x_2, y_2 = segments

            d_x = 1 if x_2 >= x_1 else -1
            d_y = 1 if y_2 >= y_1 else -1

            for x in range(x_1, x_2 + d_x, d_x):
                for y in range(y_1, y_2 + d_y, d_y):
                    try:
                        _map[y][(x - min_x)] = "#"
                    except IndexError as err:
                        print(min_x, max_x)
                        print(y, x, x - min_x)
                        raise err

    _map[0][500 - min_x] = "+"
    sand_start = (0, 500 - min_x)
    sand_pos = (0, 500 - min_x)
    #print_map(_map)
    counter = 0
    while True:
        y, x = sand_pos
        # Test sand pos down
        d_y = y + 1
        d_x = x

        if d_y > max_y:
            return counter

        if _map[d_y][d_x] == ".":
            sand_pos = (d_y, d_x)
            continue
        # Test sand pos left
        d_x = x - 1

        if d_x < 0:
            return counter
        
        if _map[d_y][d_x] == ".":
            sand_pos = (d_y, d_x)
            continue

        # Test sand pos right
        d_x = x + 1
        if d_x > (max_x - min_x):
            return counter
        
        if _map[d_y][d_x] == ".":
            sand_pos = (d_y, d_x)
            continue

        _map[y][x] = "o"
        sand_pos = sand_start
        counter += 1


def print_map(_map):
    print("  " + "".join(str(i) for i in range(len(_map[0]))))
    for i, row in enumerate(_map):
        print(i, "".join(row))


def solve_2(path: str) -> Any:
    data = read_lines(path)
    max_y = 0
    for line in data:
        for (x, y) in line:
            max_y = max(max_y, y)
    max_y += 2
    _map = defaultdict(lambda: ".")

    for line in data:
        for i, segments in enumerate(line[1:], start=1):
            x_1, y_1 = line[i - 1]
            x_2, y_2 = segments

            d_x = 1 if x_2 >= x_1 else -1
            d_y = 1 if y_2 >= y_1 else -1

            for x in range(x_1, x_2 + d_x, d_x):
                for y in range(y_1, y_2 + d_y, d_y):
                    _map[(x, y)] = "#"

    sand_start = (500, 0)
    sand_pos = sand_start
    _map[sand_start] = "+"

    counter = 0
    while True:
        x, y = sand_pos

        # Test sand pos down
        dx = x
        dy = y + 1

        if dy == max_y:
            _map[(x, y)] = "o"
            sand_pos = sand_start
            counter += 1
            continue

        if _map[(dx, dy)] == ".":
            sand_pos = (dx, dy)
            continue
        
        # Test sand pos left
        dx = x - 1

        if _map[(dx, dy)] == ".":
            sand_pos = (dx, dy)
            continue

        # Test sand pos right
        dx = x + 1
        if _map[(dx, dy)] == ".":
            sand_pos = (dx, dy)
            continue

        if (x, y) == (500, 0):
            counter += 1
            return counter

        _map[(x, y)] = "o"
        sand_pos = sand_start
        counter += 1


if __name__ == "__main__":
    print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: {solve_2('example.txt')}")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: {solve_2('input.txt')}")
