def solve(input_file: str) -> int:
    with open(input_file, "r") as f:
        data = [int(line.strip()) for line in f.readlines()]

    current = data.pop(0)
    count = 0
    for line in data:
        if line > current:
            count += 1
        current = line

    return count


if __name__ == "__main__":
    result = solve("input.txt")
    print(f"\nThere are {result} sums that are larger than the previous sum\n")
