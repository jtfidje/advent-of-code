import re
from dataclasses import dataclass
from pathlib import Path

from advent_of_code import utils
from aoc_2025_05 import DATA_PATH


@dataclass
class Range:
    start: int
    stop: int


def parse_ranges(data: str) -> list[Range]:
    return sorted(
        map(
            lambda range_: Range(int(range_[0]), int(range_[1])),
            re.findall(r"(\d+)-(\d+)", data),
        ),
        key=lambda range_: range_.start,
    )


def aggregate_ranges(ranges: list[Range]):
    agg = []
    curr = ranges[0]
    for r in ranges[1:]:
        if r.start > curr.stop:
            agg.append(curr)
            curr = r

        elif r.start <= curr.stop:
            curr.stop = max(r.stop, curr.stop)

    agg.append(curr)
    return agg


@utils.performance_timer
def solve_1(path: Path):
    range_data, id_data = utils.read_data(path).split("\n\n")
    ranges = parse_ranges(range_data)
    ranges = aggregate_ranges(ranges)

    fresh = 0
    for num in set(sorted(map(int, id_data.split()))):
        for range_ in ranges:
            if num >= range_.start and num <= range_.stop:
                fresh += 1
                break

    return fresh


@utils.performance_timer
def solve_2(path: Path):
    data = utils.read_data(path)
    range_data, _ = data.split("\n\n")
    ranges = parse_ranges(range_data)
    ranges = aggregate_ranges(ranges)

    return sum(range_.stop - range_.start + 1 for range_ in ranges)


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
    print()
    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
