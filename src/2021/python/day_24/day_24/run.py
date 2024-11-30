from itertools import permutations
import sys
from typing import List

def read_lines(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip().split(" ") for line in lines]
        return lines


def run_alu(instructions, input_number):
    input_number = list(map(int, str(input_number)))
    register = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    for instruction in instructions:
        command = instruction[0]

        if command == "inp":
            register[instruction[1]] = input_number.pop(0)
            continue

        var_1, var_2 = instruction[1:]
        val_1 = register[var_1]

        if var_2 in register:
            val_2 = register[var_2]
        else:
            val_2 = int(var_2)


        if command == "add":
            register[var_1] = val_1 + val_2

        elif command == "mul":
            register[var_1] = val_1 * val_2
        
        elif command == "div":
            if val_2 == 0:
                print(f"INVALID VALUES FOR DIV: {val_1} / {val_2}")
                sys.exit(1)
            register[var_1] = val_1 // val_2
        
        elif command == "mod":
            if val_1 < 0 or val_2 <= 0:
                print(f"INVALID VALUES FOR MOD: {val_1} % {val_2}")
                sys.exit(1)
            register[var_1] = val_1 % val_2
        
        elif command == "eql":
            register[var_1] = int(val_1 == val_2)

    return register["z"]


def rolling_number(n, _max=3):
    return ((n -1) % _max + 1)


def generate_numbers(size, depth=1):
    if depth == size:
        for i in range(1, 10):
            yield str(i)
    else:
        for i in range(1, 10):
            numbers = generate_numbers(size, depth=depth + 1)
            for j in numbers: 
                yield str(i) + j


def solve_1(path: str):
    data = read_lines(path)
    
    max_model = 0
    for i, input_number in enumerate(generate_numbers(14)):
        input_number = input_number + max(input_number) * 5
        if i % 100_000 == 0:
            print(f"Running {i}:", input_number)
        z = run_alu(data, input_number)
        if z == 0:
            print("Found valid model number:", input_number)
            max_model = max(max_model, int(input_number))
    
    return max_model


def solve_2(path: str):
    data = read_lines(path)
    ...


if __name__ == "__main__":
    path = "input.txt"
    ans_1_input = solve_1(path)
    ans_2_input = solve_2(path)

    print(f"Problem 1: {ans_1_input}")
    print(f"Problem 2: {ans_2_input}")
