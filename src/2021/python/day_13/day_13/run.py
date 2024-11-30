import numpy as np
from typing import List

def read_lines(path: str) -> List[str]:
    with open(path, "r") as f:
        return f.read()
        #lines = [line for line in f.readlines()]
        #lines = [line.strip() for line in lines]
        #return lines


def solve_1(path: str) -> int:
    data = read_lines(path)
    folds, rules = data.split("\n\n")
    folds = [list(map(int, line.split(","))) for line in folds.split("\n")]
    rules = rules.split("\n")
    rules = [(line.split("=")[0][-1], int(line.split("=")[-1])) for line in rules if line]

    max_x = max(fold[0] for fold in folds) + 1
    max_y = max(fold[1] for fold in folds) + 1

    paper = np.zeros((max_y, max_x), dtype=np.int32)
    
    for fold in folds:
        x, y = fold
        paper[y][x] = 1


    for (axis, line) in rules:
        if axis == "x":
            _left = paper[:, :line]
            _right = paper[:, line + 1:]
            _right = np.flip(_right, axis=1)

            paper = np.bitwise_or(_left, _right)
        
        elif axis == "y":
            _top = paper[:line, :]
            _bottom = paper[line + 1:, :]
            _bottom = np.flip(_bottom, axis=0)

            paper = np.bitwise_or(_top, _bottom)
        
        break

    return np.sum(paper)


def solve_2(path: str) -> int:
    data = read_lines(path)
    folds, rules = data.split("\n\n")
    folds = [list(map(int, line.split(","))) for line in folds.split("\n")]
    rules = rules.split("\n")
    rules = [(line.split("=")[0][-1], int(line.split("=")[-1])) for line in rules if line]

    max_x = max(fold[0] for fold in folds) + 1
    max_y = max(fold[1] for fold in folds) + 1

    paper = np.zeros((max_y, max_x), dtype=np.int32)
    
    for fold in folds:
        x, y = fold
        paper[y][x] = 1


    for (axis, line) in rules:
        if axis == "x":
            _left = paper[:, :line]
            _right = paper[:, line + 1:]
            _right = np.flip(_right, axis=1)

            paper = np.bitwise_or(_left, _right)
        
        elif axis == "y":
            _top = paper[:line, :]
            _bottom = paper[line + 1:, :]
            _bottom = np.flip(_bottom, axis=0)

            paper = np.bitwise_or(_top, _bottom)

    for row in paper:
        _row = "".join([str(x) for x in row])
        _row = _row.replace("0", " ").replace("1", "#")
        print(_row)


if __name__ == "__main__":
    path = "example.txt"
    ans_1_example = solve_1(path)    
    ans_2_example = solve_2(path)

    path = "input.txt"
    ans_1_input = solve_1(path)
    ans_2_input = solve_2(path)
    
    print(f"Example 1: {ans_1_example}")
    print(f"Example 2: {ans_2_example}")
    print("\n- - -\n")
    print(f"Problem 1: {ans_1_input}")
    print(f"Problem 2: {ans_2_input}")
