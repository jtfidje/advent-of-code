import re

def read_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def solve_1(path: str) -> int:
    document = read_lines(path)
    calibration_sum = 0
    for line in document:
        numbers = [char for char in line if char.isdigit()]
        calibration_number = int(numbers[0] + numbers[-1])
        calibration_sum += calibration_number
    return calibration_sum


def solve_2(path: str) -> int:
    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    
    pattern = f"(?=({'|'.join(number_map)}|\d))"
    document = read_lines(path)
    calibration_sum = 0
    for line in document:
        numbers = []
        for match in re.finditer(pattern, line):
            res = match[1]
            number = res if res.isdigit() else number_map[res]
            numbers.append(number) 
        
        calibration_number = int(numbers[0] + numbers[-1])
        calibration_sum += calibration_number
    return calibration_sum


if __name__ == "__main__":
    print(f"Example 1: {solve_1('example_1.txt')}")
    print(f"Example 2: {solve_2('example_2.txt')}")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: {solve_2('input.txt')}")
