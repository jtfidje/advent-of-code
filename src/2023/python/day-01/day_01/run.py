from typing import Any

def read_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines

def solve_1(path: str) -> Any:
    data = read_lines(path)
    import string
    _sum = 0
    for line in data:
        number = ""
        for char in line:
            if char in string.digits:
                number += char
        _sum += int(number[0] + number[-1])
    return _sum


def solve_2(path: str) -> Any:
    number_map = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    data = read_lines(path)
    import string
    _sum = 0
    for line in data:
        numbers = {}
        for key, value in number_map.items():
            _line = line
            while key in _line:
                numbers[_line.index(key)] = value
                _line = _line.replace(key, "-" * len(key), 1)
        for i, char in enumerate(line):
            if char in string.digits:
                numbers[i] = char
        sorted_keys = sorted(numbers.keys())
        _sum += int(numbers[sorted_keys[0]] + numbers[sorted_keys[-1]])
    return _sum

if __name__ == "__main__":
    #print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: {solve_2('example.txt')}")
    print("\n- - -\n")
    #print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: {solve_2('input.txt')}")
