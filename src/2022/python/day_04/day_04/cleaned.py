def read_data(path: str):
    data = []
    with open(path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            line = line.replace(",", " ")
            line = line.replace("-", " ")
            line = line.split()
            line = list(map(int, line))

            data.append(line)

    return data


def solve_1(path: str):
    data = read_data(path)
    count = 0
    for line in data:
        a, b, x, y = line

        range_1 = range(a, b + 1)
        range_2 = range(x, y + 1)

        if range_1 == range_2:
            count += 1

        elif all(num in range_2 for num in range_1):
            count += 1

        elif all(num in range_1 for num in range_2):
            count += 1

    return count


def solve_2(path: str):
    data = read_data(path)
    count = 0
    for line in data:
        a, b, x, y = line

        range_1 = range(a, b + 1)
        range_2 = range(x, y + 1)

        if range_1 == range_2:
            count += 1

        elif any(num in range_2 for num in range_1):
            count += 1

    return count


if __name__ == "__main__":
    print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: {solve_2('example.txt')}")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: {solve_2('input.txt')}")
