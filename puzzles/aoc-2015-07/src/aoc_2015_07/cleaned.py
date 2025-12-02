import re
from pathlib import Path
from dataclasses import dataclass

from advent_of_code.utils import read_lines
from aoc_2015_07 import DATA_PATH

OP_MAP = {
    "SET": lambda x: x,
    "NOT": lambda x: ~x + (1 << 16),
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "LSHIFT": lambda x, y: x << y,
    "RSHIFT": lambda x, y: x >> y,
}

@dataclass
class Connection:
    op: str
    out: str
    x: str
    y: str | None

def get_connections(path: str | Path) -> list[Connection]:
    data = read_lines(path)

    connections = []
    for line in data:
        if (res := re.search(r"(.+) (AND|LSHIFT|RSHIFT|OR) (.+) -> (.+)", line)):
            x, op, y, out = res.groups()
        else:
            x, out = re.search(r"^(?:NOT )?(\w+|\d+) -> (.+)$", line).groups()  # type: ignore
            if line.startswith("NOT"):
                op = "NOT"
            else:
                op = "SET"

            y = None

        connections.append(Connection(op, out, x, y))
    
    return connections

def wire_circuit(connections: list[Connection]):
    circuit: dict[str, int] = {}
    while connections:
        con = connections.pop(0)

        try:
            if con.op in {"AND", "LSHIFT", "RSHIFT", "OR"}:
                x = int(circuit.get(con.x, con.x))
                y = int(circuit.get(con.y, con.y))  # type: ignore
                circuit[con.out] = OP_MAP[con.op](x, y)
            else:
                x = int(circuit.get(con.x, con.x))
                circuit[con.out] = OP_MAP[con.op](x)
        except ValueError:
            connections.append(con)
    
    return circuit

def solve_1(path: Path):
    circuit = wire_circuit(connections=get_connections(path))
    return circuit["a"]


def solve_2(path: Path):
    circuit = wire_circuit(connections=get_connections(path))

    connections = get_connections(path)
    for con in connections:
        if con.out == "b" and con.op == "SET":
            con.x = str(circuit["a"])

    circuit = wire_circuit(connections=connections)
    return circuit["a"]


if __name__ == "__main__":
    answer = solve_1(DATA_PATH / "input.txt")
    print(f"Problem 1: {answer}")

    answer = solve_2(DATA_PATH / "input.txt")
    print(f"Problem 2: {answer}")
