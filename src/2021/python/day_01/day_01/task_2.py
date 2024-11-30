def solve(input_file: str) -> int:
    with open(input_file, "r") as f:
        data = [int(line.strip()) for line in f.readlines()]

    count = 0
    for i in range(0, len(data) - 3):
        window_1 = sum(data[i: i + 3])
        window_2 = sum(data[i + 1: i + 4])

        if window_2 > window_1:
            count += 1

    return count


if __name__ == "__main__":
    result = solve("input.txt")
    print(f"\nThere are {result} sums that are larger than the previous sum\n")