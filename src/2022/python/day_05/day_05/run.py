import json
from collections import defaultdict
from functools import reduce


def json_print(obj):
    print(json.dumps(obj, indent=2))


def read_lines(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.replace("\n", "") for line in lines]
        return lines


def read_numbers(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return list(map(int, lines))


def solve_1(path: str):
    data = read_lines(path)
    stacks = []
    while not data[0].startswith(" 1"):
        stacks.append(data.pop(0))
    
    col_count = list(map(int, data.pop(0).strip().split()))[-1]

    data = data[1:]

    columns = defaultdict(list)
    for row in stacks:
        for i in range(col_count):
            element = row[1 + (i * 4)].strip()
            
            if element:
                columns[i + 1].append(element)

    for line in data:
        elements = line.split()
        move_count = int(elements[1])
        x, y = int(elements[-3]), int(elements[-1])

        for i in range(move_count):
            element = columns[x].pop(0)
            columns[y].insert(0, element)

    message = ""
    for i in range(col_count):
        message += columns[i + 1][0]
    return message

    

def solve_2(path: str):
    data = read_lines(path)
    stacks = []
    while not data[0].startswith(" 1"):
        stacks.append(data.pop(0))
    
    col_count = list(map(int, data.pop(0).strip().split()))[-1]

    data = data[1:]

    columns = defaultdict(list)
    for row in stacks:
        for i in range(col_count):
            element = row[1 + (i * 4)].strip()
            
            if element:
                columns[i + 1].append(element)

    for line in data:
        elements = line.split()
        move_count = int(elements[1])
        x, y = int(elements[-3]), int(elements[-1])

        temp = []
        for i in range(move_count):
            element = temp.append(columns[x].pop(0))
        
        columns[y] = temp + columns[y]

    message = ""
    for i in range(col_count):
        message += columns[i + 1][0]
    return message


if __name__ == "__main__":
    print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: {solve_2('example.txt')}")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: {solve_2('input.txt')}")
