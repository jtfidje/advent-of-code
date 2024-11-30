import json
from collections import defaultdict
from functools import reduce
from typing import Any


class Block:
    def __init__(self, left: int, bottom: int, pattern: list[list[str]]):
        self.points = []
        self.left = left
        self.bottom = bottom
        self.pattern = pattern
        self.points = []

        for y, row in enumerate(self.pattern[::-1], start=self.bottom):
            for x, col in enumerate(row, start=self.left):
                if col == "#":
                    self.points.append((x, y))
        
    @property
    def top(self):
        return max(y for (_, y) in self.points)

    @property
    def right(self):
        return max(x for (x, _) in self.points)


BLOCKS = [
    [
        list("####")
    ],
    [
        list(".#."),
        list("###"),
        list(".#.")
    ],
    [
        list("..#"),
        list("..#"),
        list("###"),
    ],
    [
        ["#"],
        ["#"],
        ["#"],
        ["#"],
    ],
    [
        list("##"),
        list("##"),
    ]
]


_map = defaultdict(lambda: ".")


def json_print(obj: dict | list) -> None:
    print(json.dumps(obj, indent=4))


def read_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def read_numbers(path: str) -> list[int]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return list(map(int, lines))


def print_map(_map, current_block=None):
    if current_block is not None:
        _map.update({point: "@" for point in current_block.points})

    max_y = max((y for (_, y) in _map.keys()), default=3)
    for y in range(max_y, 0, -1):
        line = ""
        for x in range(1, 8):
            line += _map[(x, y)]
        print(line)
    print()
    


def solve_1(path: str) -> Any:
    _map = defaultdict(lambda: ".")
    with open(path) as f:
        data = f.read().strip()

    stopped_blocks = []
    step = 0
    current_block = None
    while len(stopped_blocks) < 2022:
        pattern = BLOCKS[len(stopped_blocks) % len(BLOCKS)]

        max_y = max((block.top for block in stopped_blocks), default=0)
        current_block = Block(
            bottom=max_y + 5,  # Start one higher
            left=3,
            pattern=pattern
        )
        while current_block is not None:
            # Move block down
            temp_block = Block(
                left=current_block.left,
                bottom=current_block.bottom - 1,
                pattern=current_block.pattern
            )

            if temp_block.bottom == 0 or any(point in _map for point in temp_block.points):
                for point in current_block.points:
                    _map[point] = "#"
                stopped_blocks.append(current_block)
                current_block = None
                break

            current_block = temp_block

            # Try to shift block
            shift = data[step % len(data)]
            step += 1
            if shift == ">":
                if current_block.right == 7:
                    continue

                temp_block = Block(
                    left=current_block.left + 1,
                    bottom=current_block.bottom,
                    pattern=current_block.pattern
                )

            elif shift == "<":
                if current_block.left == 1:
                    continue

                temp_block = Block(
                    left=current_block.left - 1,
                    bottom=current_block.bottom,
                    pattern=current_block.pattern
                )

            for point in temp_block.points:
                if point in _map:
                    break
            else:
                current_block = temp_block
    
    return max((block.top for block in stopped_blocks), default=0)


def solve_2(path: str) -> Any:
    _map = defaultdict(lambda: ".")
    with open(path) as f:
        data = f.read().strip()

    stopped_blocks = []
    step = 0
    current_block = None
    while len(stopped_blocks) < 2022:
        pattern = BLOCKS[len(stopped_blocks) % len(BLOCKS)]

        max_y = max((block.top for block in stopped_blocks), default=0)
        current_block = Block(
            bottom=max_y + 5,  # Start one higher
            left=3,
            pattern=pattern
        )
        while current_block is not None:
            # Move block down
            temp_block = Block(
                left=current_block.left,
                bottom=current_block.bottom - 1,
                pattern=current_block.pattern
            )

            if temp_block.bottom == 0 or any(point in _map for point in temp_block.points):
                for point in current_block.points:
                    _map[point] = "#"
                stopped_blocks.append(current_block)
                current_block = None
                break

            current_block = temp_block

            # Try to shift block
            shift = data[step % len(data)]
            step += 1
            if shift == ">":
                if current_block.right == 7:
                    continue

                temp_block = Block(
                    left=current_block.left + 1,
                    bottom=current_block.bottom,
                    pattern=current_block.pattern
                )

            elif shift == "<":
                if current_block.left == 1:
                    continue

                temp_block = Block(
                    left=current_block.left - 1,
                    bottom=current_block.bottom,
                    pattern=current_block.pattern
                )

            for point in temp_block.points:
                if point in _map:
                    break
            else:
                current_block = temp_block
    
    return max((block.top for block in stopped_blocks), default=0)


if __name__ == "__main__":
    #print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: {solve_2('example.txt')}")
    print("\n- - -\n")
    #print(f"Problem 1: {solve_1('input.txt')}")
    #print(f"Problem 2: {solve_2('input.txt')}")
