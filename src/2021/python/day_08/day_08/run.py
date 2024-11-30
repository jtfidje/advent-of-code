from collections import defaultdict
from typing import List


def read_lines(path: str) -> List[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def solve_1(path: str) -> int:
    """
    Totally did not understand that I could just count the unique numbers in Part 1

    So... I basically did Part 2 in Part 1....
    """

    data = read_lines(path)
    digit_count = defaultdict(int)
    for line in data:
        patterns, output = map(lambda x: x.split(" "), line.split(" | "))

        wires = {}
        temp_unique_segments = defaultdict(set)
        temp_segment_count_patterns = defaultdict(list)
        digits = {}
        for pattern in patterns:
            i = len(pattern)
            temp_unique_segments[i] = temp_unique_segments[i].union(pattern)
            temp_segment_count_patterns[i].append(set(pattern))

            # 1 Use two segments
            # 7 Use three segments
            # 4 Use four segments
            # 8 Use seven segments
            if i == 2:
                digits[1] = set(pattern)
            elif i == 3:
                digits[7] = set(pattern)
            elif i == 4:
                digits[4] = set(pattern)
            elif i == 7:
                digits[8] = set(pattern)

        # Rules
        # Wire 1 is the letter present in 7 that's not present in 1
        wires[1] = digits[7].difference(digits[1]).pop()

        # Wire 6 is the letter present in 1 that's also present in 0, 6 and 9
        # Digit 6 is the pattern where only 1 segment intersects with digit 1
        for pattern in temp_segment_count_patterns[6]:
            intersection = pattern.intersection(digits[1])
            if len(intersection) == 1:
                digits[6] = pattern
                wires[6] = intersection.pop()
                break

        # Wire 3 is the letter present in 1 that's not present in 6
        wires[3] = next(letter for letter in digits[1] if letter not in digits[6])

        # Digit 2 is the pattern where only 2 segments intersects with digit 4
        # Wire 4 is the letter in the intersection of digits 2 and 4 that is not wire 3
        for pattern in temp_segment_count_patterns[5]:
            intersection = pattern.intersection(digits[4])
            if len(intersection) == 2:
                digits[2] = pattern
                intersection.remove(wires[3])
                wires[4] = intersection.pop()
                break

        # Digit 5 is the remaining 5-segment pattern where only wire 6 is present, the other is digit 3
        for pattern in temp_segment_count_patterns[5]:
            if pattern == digits[2]:
                continue
            
            if digits[1].issubset(pattern):
                digits[3] = pattern
            else:
                digits[5] = pattern

        # Digit 9 is the remaining 6-segment digit that is a superset of 3, the other is 0
        for pattern in temp_segment_count_patterns[6]:
            if pattern == digits[6]:
                continue

            if digits[3].issubset(pattern):
                digits[9] = pattern
            else:
                digits[0] = pattern

        reverse_digits = {"".join(sorted(value)): key for key, value in digits.items()}
        for digit in output:
            _sorted = "".join(sorted(digit))
            try:
                num = reverse_digits[_sorted]
            except KeyError:
                num = next(i for i in range(10) if i not in digits.keys())
            digit_count[num] += 1

    return sum(
        [
            digit_count[1],
            digit_count[4],
            digit_count[7],
            digit_count[8],
        ]
    )


def solve_2(path: str) -> int:
    data = read_lines(path)
    digit_count = defaultdict(int)
    part_2_sum = 0
    for line in data:
        patterns, output = map(lambda x: x.split(" "), line.split(" | "))

        wires = {}
        temp_unique_segments = defaultdict(set)
        temp_segment_count_patterns = defaultdict(list)
        digits = {}
        for pattern in patterns:
            i = len(pattern)
            temp_unique_segments[i] = temp_unique_segments[i].union(pattern)
            temp_segment_count_patterns[i].append(set(pattern))

            # 1 Use two segments
            # 7 Use three segments
            # 4 Use four segments
            # 8 Use seven segments
            if i == 2:
                digits[1] = set(pattern)
            elif i == 3:
                digits[7] = set(pattern)
            elif i == 4:
                digits[4] = set(pattern)
            elif i == 7:
                digits[8] = set(pattern)

        # Rules
        # Wire 1 is the letter present in 7 that's not present in 1
        wires[1] = digits[7].difference(digits[1]).pop()

        # Wire 6 is the letter present in 1 that's also present in 0, 6 and 9
        # Digit 6 is the pattern where only 1 segment intersects with digit 1
        for pattern in temp_segment_count_patterns[6]:
            intersection = pattern.intersection(digits[1])
            if len(intersection) == 1:
                digits[6] = pattern
                wires[6] = intersection.pop()
                break

        # Wire 3 is the letter present in 1 that's not present in 6
        wires[3] = next(letter for letter in digits[1] if letter not in digits[6])

        # Digit 2 is the pattern where only 2 segments intersects with digit 4
        # Wire 4 is the letter in the intersection of digits 2 and 4 that is not wire 3
        for pattern in temp_segment_count_patterns[5]:
            intersection = pattern.intersection(digits[4])
            if len(intersection) == 2:
                digits[2] = pattern
                intersection.remove(wires[3])
                wires[4] = intersection.pop()
                break

        # Digit 5 is the remaining 5-segment pattern where only wire 6 is present, the other is digit 3
        for pattern in temp_segment_count_patterns[5]:
            if pattern == digits[2]:
                continue
            
            if digits[1].issubset(pattern):
                digits[3] = pattern
            else:
                digits[5] = pattern

        # Digit 9 is the remaining 6-segment digit that is a superset of 3, the other is 0
        for pattern in temp_segment_count_patterns[6]:
            if pattern == digits[6]:
                continue

            if digits[3].issubset(pattern):
                digits[9] = pattern
            else:
                digits[0] = pattern

        reverse_digits = {"".join(sorted(value)): key for key, value in digits.items()}
        for digit in output:
            _sorted = "".join(sorted(digit))
            try:
                num = reverse_digits[_sorted]
            except KeyError:
                num = next(i for i in range(10) if i not in digits.keys())
            digit_count[num] += 1

    
        res = []
        for digit in output:
            _sorted = "".join(sorted(digit))
            try:
                num = reverse_digits[_sorted]
            except KeyError:
                num = next(i for i in range(10) if i not in digits.keys())

            res.append(str(num))
        res = int("".join(res))

        part_2_sum += res

    return part_2_sum


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
