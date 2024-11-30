from functools import cache
from itertools import permutations
import sys
from typing import List

def read_lines(path: str):
    with open(path, "r") as f:
        data = f.read()
        programs = data.split("\n\n")
        for i, program in enumerate(programs):
            programs[i] = program.split("\n")

    return programs

def execute_program(register, program, inp):
    op = program.pop(0)
    _, reg = op.split(" ")
    
    register[reg] = inp

    for prog in program:
        op, a, b = prog.split(" ")

        try:
            b = int(b)
        except ValueError:
            b = register[b]

        if op == "add":
            register[a] += b

        elif op == "mul":
            register[a] *= b

        elif op == "div":
            if b == 0:
                continue
            else:
                register[a] = int(register[a] / b)

        elif op == "mod":
            if b == 0:
                continue
            else:
                register[a] %= b

        elif op == "eql":
            register[a] = int(register[a] == b)


def solve_1(path: str):
    data = read_lines(path)
    number = 10 ** 14
    
    while True:
        register = {"w": 0, "x": 0, "y": 0, "z": 0}
        number -= 1
        if number % 1000 == 0:
            print(number)
        _input = str(number)
        if "0" in _input:
            continue
        for i, program in enumerate(data):
            inp = int(_input[i])
            execute_program(register, program[:], inp)
        if register["z"] == 0:
            break

    
    print(number)



def solve_2(path: str):
    data = read_lines(path)
    ...


if __name__ == "__main__":
    path = "input.txt"
    ans_1_input = solve_1(path)
    ans_2_input = solve_2(path)

    print(f"Problem 1: {ans_1_input}")
    print(f"Problem 2: {ans_2_input}")
