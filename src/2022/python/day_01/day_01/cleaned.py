from functools import reduce


def read_data(path: str) -> list[list[int]]:
    with open(path, "r") as f:
        data = f.read().strip().split("\n\n")
    data = list(map(lambda x: x.split("\n"), data))
    data = list(map(lambda x: list(map(int, x)), data))
    return data


def solve_1(path: str) -> int:
    data = read_data(path)

    return reduce(max, map(sum, data))


def solve_2(path: str) -> int:
    data = read_data(path)

    data = sorted(map(sum, data))
    return sum(data[-3:])


if __name__ == "__main__":
    print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: {solve_2('example.txt')}")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: {solve_2('input.txt')}")