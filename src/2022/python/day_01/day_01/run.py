
def read_lines(path: str):
    with open(path, "r") as f:
        data = f.read().split("\n\n")

        elves = []
        for line in data:
            line = line.strip().split("\n")
            elves.append(list(map(int, line)))

        return elves


def solve_1(path: str):
    _max = 0
    data = read_lines(path)
    for line in data:
        if sum(line) > _max:
            _max = sum(line)
    return _max


def solve_2(path: str):
    _max = []
    data = read_lines(path)
    for line in data:
        _max.append(sum(line))

    res = sorted(_max)

    return sum(res[-3:])


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
