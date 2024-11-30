import numpy as np
import pyperclip
from typing import List

def read_lines(path: str) -> List[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        numbers = list(map(int, lines[0].split(",")))
        return numbers


def solve_1(path: str) -> int:
    data = read_lines(path)
    data = np.array(data)    
    unique_positions = set(data)

    fuel_costs = []
    for pos in unique_positions:
        deltas = data - pos
        deltas = np.absolute(deltas)
        fuel_costs.append(np.sum(deltas))

    return min(fuel_costs)


def solve_2(path: str) -> int:
    data = read_lines(path)
    data = np.array(data)    
    unique_positions = range(max(data))

    fuel_costs = []
    for pos in unique_positions:
        deltas = data - pos
        deltas = np.absolute(deltas)
        fuel_costs.append(np.sum(list(map(lambda x: sum(range(1, x + 1)), deltas))))

    return min(fuel_costs)



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

    #pyperclip.copy(ans_1_input)
    # pyperclip.copy(ans_2_input)
