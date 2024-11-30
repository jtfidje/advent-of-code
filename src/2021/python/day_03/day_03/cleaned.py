import sys
from typing import List, Tuple


def read_diagnostics_report(path: str) -> List[str]:
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]


def transpose_report(diagnostics_report: List[str]) -> List[str]:
    """Transpose from list of 'rows' to list of 'columns'"""
    return [
        [line[i] for line in diagnostics_report]
        for i in range(len(diagnostics_report[0]))
    ]


def parse_report(diagnostics_report: List[str]) -> Tuple[List[str], List[str]]:
    transposed_report = transpose_report(diagnostics_report)
    
    most_common_bits = []
    least_common_bits = []
    for line in transposed_report:
        num_active_bits = line.count("1")
        num_inactive_bits = line.count("0")

        if num_active_bits >= num_inactive_bits:
            most_common_bits.append("1")
            least_common_bits.append("0")
        else:
            most_common_bits.append("0")
            least_common_bits.append("1")

    return (most_common_bits, least_common_bits)

def calculate_gamma_epsilon(diagnostics_report: List[str]) -> Tuple[int, int]:
    most_common_bits, least_common_bits = parse_report(diagnostics_report)

    gamma_rate = int("".join(most_common_bits), 2)
    epsilon_rate = int("".join(least_common_bits), 2)

    return gamma_rate, epsilon_rate


def calculate_life_support_rating(diagnostics_report: List[str], rating_type: str) -> int:
    filtered_report = diagnostics_report[:]
    for i in range(len(diagnostics_report[0])):
        if rating_type == "oxygen":
            bits, _ = parse_report(filtered_report)
        elif rating_type == "co2":
            _, bits = parse_report(filtered_report)
        else:
            print(f"Unknown rating type '{rating_type}'. Panic!")
            sys.exit(1)
        
        filtered_report = [line for line in filtered_report if line[i] == bits[i]]
        if len(filtered_report) == 1:
            break

    return int("".join(filtered_report), 2)


def solve_1(path: str) -> int:
    diagnostics_report = read_diagnostics_report(path)
    gamma_rate, epsilon_rate = calculate_gamma_epsilon(diagnostics_report)

    return gamma_rate * epsilon_rate


def solve_2(path: str) -> int:
    diagnostics_report = read_diagnostics_report(path)
    oxygen = calculate_life_support_rating(diagnostics_report, rating_type="oxygen")
    co2 = calculate_life_support_rating(diagnostics_report, rating_type="co2")

    return oxygen * co2


if __name__ == "__main__":
    path = "input.txt"

    ans_1 = solve_1(path)
    print(f"Problem 1: {ans_1}")
    
    ans_2 = solve_2(path)
    print(f"Problem 2: {ans_2}")
