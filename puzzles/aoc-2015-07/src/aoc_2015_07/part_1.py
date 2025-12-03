# flake8: noqa: F401

import re
from pathlib import Path

from advent_of_code import utils
from aoc_2015_07 import DATA_PATH

OP_MAP = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "LSHIFT": lambda x, y: x << y,
    "RSHIFT": lambda x, y: x >> y,
}


def solve(path: str | Path):
    data = utils.read_lines(path)
    circuit = {}

    connections = []
    for line in data:
        if res := re.search(r"(.+) (AND|LSHIFT|RSHIFT|OR) (.+) -> (.+)", line):
            x, op, y, out = res.groups()

            connections.append(
                {
                    "op": op,
                    "out": out,
                    "x": x,
                    "y": y,
                }
            )
        else:
            x, out = re.search(r"^(?:NOT )?(\w+|\d+) -> (.+)$", line).groups()  # type: ignore
            if line.startswith("NOT"):
                op = "NOT"
            else:
                op = "SET"

            connections.append({"op": op, "out": out, "x": x})

    while connections:
        con = connections.pop(0)

        match con["op"]:
            case "SET" | "NOT":
                if con["x"].isnumeric():
                    x = int(con["x"])
                elif con["x"] in circuit:
                    x = circuit[con["x"]]
                else:
                    connections.append(con)
                    continue

                if con["op"] == "NOT":
                    x = ~x + (1 << 16)

                circuit[con["out"]] = x

            case "AND" | "LSHIFT" | "RSHIFT" | "OR":
                if con["x"].isnumeric():
                    x = int(con["x"])
                elif con["x"] in circuit:
                    x = circuit[con["x"]]
                else:
                    connections.append(con)
                    continue

                if con["y"].isnumeric():
                    y = int(con["y"])
                elif con["y"] in circuit:
                    y = circuit[con["y"]]
                else:
                    connections.append(con)
                    continue

                circuit[con["out"]] = OP_MAP[con["op"]](x, y)

    return circuit["a"]


if __name__ == "__main__":
    answer = solve(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")
