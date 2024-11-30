
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
    data = read_lines(path)
    count = 0
    for line in data:
        line = line.split(",")
        a, b = list(map(int, line[0].split("-")))
        x, y = list(map(int, line[1].split("-")))

        range_1 = set(range(a, b + 1))
        range_2 = set(range(x, y + 1))

        if range_1 == range_2:
            count += 1

        else:
            if all(num in range_2 for num in range_1):
                count += 1

            if all(num in range_1 for num in range_2):
                count += 1

    return count


def solve_2(path: str):
    data = read_lines(path)
    count = 0
    for line in data:
        line = line.split(",")
        a, b = list(map(int, line[0].split("-")))
        x, y = list(map(int, line[1].split("-")))

        range_1 = set(range(a, b + 1))
        range_2 = set(range(x, y + 1))

        if range_1 == range_2:
            count += 1
        
        else:
            if any(num in range_2 for num in range_1):
                count += 1

            #if any(num in range_1 for num in range_2):
            #    count += 1

    return count


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
