# flake8: noqa: F401
import multiprocessing
import re
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def solve(path: str | Path):
    raw = utils.read_data(path)

    program = list(
        map(int, re.search(r"Program: ((\d,?)+)", raw).groups()[0].split(","))  # type: ignore
    )

    cores = 8
    i = 100_000
    while True:
        inputs = [(a, program) for a in range(i, i + cores)]
        with multiprocessing.Pool(cores) as pool:
            results = pool.map(solver, inputs)

        for res in results:
            if res:
                print(res)
                break

        i += cores


def solver(inp: tuple[int, list[int]]) -> int | None:
    register_a, program = inp

    register_a = register_a
    register_b = 0
    register_c = 0

    combo_map = {
        0: lambda: 0,
        1: lambda: 1,
        2: lambda: 2,
        3: lambda: 3,
        4: lambda: register_a,
        5: lambda: register_b,
        6: lambda: register_c,
        7: lambda: None,
    }

    output = []
    pointer = -2
    increase_pointer = True
    while True:
        if increase_pointer:
            pointer += 2
        else:
            increase_pointer = True

        if pointer >= len(program):
            break

        opcode, operand = program[pointer], program[pointer + 1]

        match opcode:
            case 0:
                # "adv" Divide register_a by combo operand. save to register a
                register_a = register_a // (2 ** combo_map[operand]())

            case 1:
                # "bxl" Bitwise XOR of register_b and literal operand save to register b
                register_b = register_b ^ operand

            case 2:
                # "bst" combo operand mod 8 to reg b
                register_b = combo_map[operand]() % 8

            case 3:
                # "jnx" jump instruction pointer by operand of register_a != 0
                if register_a == 0:
                    continue

                # TODO: Jump instruction pointer
                increase_pointer = False
                pointer = operand

            case 4:
                register_b = register_c ^ register_b

            case 5:
                output.append(combo_map[operand]() % 8)

            case 6:
                register_b = register_a // (2 ** combo_map[operand]())

            case 7:
                register_c = register_a // (2 ** combo_map[operand]())

        if ",".join(map(str, output)) == ",".join(map(str, program)):
            return register_a

    return None


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")
