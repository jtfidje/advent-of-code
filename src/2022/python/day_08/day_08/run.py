import json
from functools import reduce
from typing import Any
import sys
sys.setrecursionlimit(1500)

def json_print(obj: dict | list) -> None:
    print(json.dumps(obj, indent=4))

def read_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [list(map(int, list(line.strip()))) for line in lines]
        return lines


def read_numbers(path: str) -> list[int]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return list(map(int, lines))


def solve_1(path: str) -> Any:
    data = read_lines(path)

    _map = [[0] * len(data[0]) for _ in data]
    
    for i in range(len(data)):
        _map[i][0] = 1
        _map[i][-1] = 1

    _map[0] = [1] * len(data[0])
    _map[-1] = [1] * len(data[0])

    for row in range(1, len(data) - 1):
        for col in range(1, len(data[0]) - 1):
            tree = data[row][col]

            i = row
            while i > 0:
                i -= 1
                if tree <= data[i][col]:
                    break
            else:
                _map[row][col] = 1

            i = row
            while i < len(data) - 1:
                i += 1
                if tree <= data[i][col]:
                    break
            else:
                _map[row][col] = 1

            j = col
            while j < len(data[0]) - 1:
                j += 1
                if tree <= data[row][j]:
                    break
            else:
                _map[row][col] = 1

            j = col
            while j > 0:
                j -= 1
                if tree <= data[row][j]:
                    break
            else:
                _map[row][col] = 1

    return sum(sum(row) for row in _map)
            

def solve_2(path: str) -> Any:
    data = read_lines(path)

    _map = [[0] * len(data[0]) for _ in data]
    
    for row in range(0, len(data)):
        for col in range(len(data[0])):
            tree = data[row][col]
            scores = [0, 0, 0, 0]

            i = row
            while i > 0:
                i -= 1
                scores[0] += 1
                if tree <= data[i][col]:
                    break

            i = row
            while i < len(data) - 1:
                i += 1
                scores[1] += 1
                if tree <= data[i][col]:
                    break

            j = col
            while j < len(data[0]) - 1:
                j += 1
                scores[2] += 1
                if tree <= data[row][j]:
                    break

            j = col
            while j > 0:
                j -= 1
                scores[3] += 1
                if tree <= data[row][j]:
                    break

            _map[row][col] = reduce(lambda x, y: x * y, scores)

    return max(max(row) for row in _map)


if __name__ == "__main__":
    print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: {solve_2('example.txt')}")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: {solve_2('input.txt')}")
