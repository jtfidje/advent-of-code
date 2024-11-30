import numpy as np
from typing import List, Tuple

InstructionType = Tuple[np.array, List[Tuple[str, int]]]


def read_fold_instructions(path: str) -> InstructionType:
    with open(path, "r") as f:
        data = f.read()
        coordinates, rules = data.split("\n\n")
        
        coordinates = [
            list(map(int, line.split(",")))
            for line in coordinates.split("\n")
        ]

        rules = [
            (fold.split("=")[0][-1], int(fold.split("=")[-1]))
            for fold in rules.split("\n") if fold
        ]    

        return np.array(coordinates), rules


def fold_vertical(paper: np.array, col: int) -> np.array:
    top = paper[:col, :]
    bottom = paper[col + 1:, :]
    bottom = np.flip(bottom, axis=0)

    return np.bitwise_or(top, bottom)


def fold_horizontal(paper: np.array, row: int) -> np.array:
    left = paper[:, :row]
    right = paper[:, row + 1:]
    right = np.flip(right, axis=1)

    return np.bitwise_or(left, right)


def print_paper(paper: np.array) -> None:
    segment = "█"

    for row in paper:
        _row = "".join([str(x) for x in row])
        _row = _row.replace("0", " ").replace("1", segment)
        print(_row)
    print("\n")


def solve_1(path: str) -> int:
    coordinates, rules = read_fold_instructions(path)
    max_x, max_y = map(lambda x: x + 1, np.max(coordinates, axis=0))

    paper = np.zeros((max_x, max_y), dtype=np.int32)
    paper[tuple(coordinates.T)] = 1
    paper = paper.T

    axis, line = rules[0]
    if axis == "x":
        paper = fold_horizontal(paper, line)
        
    elif axis == "y":
        paper = fold_vertical(paper, line)

    return np.sum(paper)


def solve_2(path: str) -> int:
    coordinates, rules = read_fold_instructions(path)
    max_x, max_y = map(lambda x: x + 1, np.max(coordinates, axis=0))

    paper = np.zeros((max_x, max_y), dtype=np.int32)
    paper[tuple(coordinates.T)] = 1
    paper = paper.T


    for (axis, line) in rules:
        if axis == "x":
            paper = fold_horizontal(paper, line)
            
        elif axis == "y":
            paper = fold_vertical(paper, line)

    print_paper(paper)


if __name__ == "__main__":
    path = "example.txt"
    ans_1_example = solve_1(path)    
    
    path = "input.txt"
    ans_1_input = solve_1(path)
    
    print(f"Example 1: {ans_1_example}")
    print()
    print(f"Problem 1: {ans_1_input}")
    print("\n- - -\n")
    solve_2(path)