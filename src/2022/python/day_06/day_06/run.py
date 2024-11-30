from functools import reduce


def read_lines(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def read_numbers(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return list(map(int, lines))


def solve_1(path: str):
    with open(path) as f:
        data = f.read().strip()

    for i in range(4, len(data)):
        if len(set(data[i - 4: i])) == 4:
            return i


def solve_2(path: str):
    with open(path) as f:
        data = f.read().strip()

    for i in range(14, len(data)):
        if len(set(data[i - 14: i])) == 14:
            return i


if __name__ == "__main__":
    print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: {solve_2('example.txt')}")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: {solve_2('input.txt')}")
