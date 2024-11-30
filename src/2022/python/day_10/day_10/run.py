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
        return lines


def read_numbers(path: str) -> list[int]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return list(map(int, lines))


def solve_1(path: str) -> Any:
    data = read_lines(path)
    operations = []
    for i, line in enumerate(data):
        if line == "noop":
            operations.append({"type": "noop", "value": 0, "counter": 1})
        else:
            op, value = line.split()
            value = int(value)
            operations.append({"type": op, "value": value, "counter": 0})


    operation = operations.pop(0)
    counter = 1
    signal_strengths = []
    x = 1
    while True:
        operation["counter"] += 1
    
        if (counter == 20 or (counter - 20) % 40 == 0):
            signal_strengths.append(counter * x)

        if operation["counter"] == 2:

            x += operation["value"]

            try:
                operation = operations.pop(0)
            except IndexError:
                break

        counter += 1

    return sum(signal_strengths)




def solve_2(path: str) -> Any:
    data = read_lines(path)
    operations = []
    for i, line in enumerate(data):
        if line == "noop":
            operations.append({"type": "noop", "value": 0, "counter": 1})
        else:
            op, value = line.split()
            value = int(value)
            operations.append({"type": op, "value": value, "counter": 0})


    crt = ""
    operation = operations.pop(0)
    counter = 0
    x = 1
    while True:
        operation["counter"] += 1

        if counter in [x - 1, x, x + 1]:
            crt += "#"
        else:
            crt += "."
        
        if operation["counter"] == 2:

            x += operation["value"]

            try:
                operation = operations.pop(0)
            except IndexError:
                break

        if counter == 39:
            crt += "\n"
            counter = -1

        counter += 1

    return crt


if __name__ == "__main__":
    print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: \n{solve_2('example.txt')}\n")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: \n{solve_2('input.txt')}\n")
