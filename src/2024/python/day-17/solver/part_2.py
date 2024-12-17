# flake8: noqa: F401
import re
from collections import defaultdict
from functools import cache
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"

register_a = 0
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


def solve(path: str | Path):
    global register_a
    global register_b
    global register_c

    raw = utils.read_data(path)

    register_a = int(re.search(r"A: (\d+)", raw).groups()[0])  # type: ignore
    register_b = int(re.search(r"B: (\d+)", raw).groups()[0])  # type: ignore
    register_c = int(re.search(r"C: (\d+)", raw).groups()[0])  # type: ignore

    program = list(
        map(int, re.search(r"Program: ((\d,?)+)", raw).groups()[0].split(","))  # type: ignore
    )

    seen = set()

    i = 0
    while True:
        pointer = -2
        increase_pointer = True

        i += 1
        register_a = i

        print(register_a)

        while pointer < len(program):
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
                    register_a = adv(register_a, operand)

                case 1:
                    # "bxl" Bitwise XOR of register_b and literal operand save to register b
                    register_b = bxl(register_b, operand)

                case 2:
                    # "bst" combo operand mod 8 to reg b
                    register_b = bst(operand)

                case 3:
                    # "jnx" jump instruction pointer by operand of register_a != 0
                    if register_a == 0:
                        continue

                    # TODO: Jump instruction pointer
                    increase_pointer = False
                    pointer = operand

                case 4:
                    register_b = bxc(register_c, register_b)

                case 5:
                    output.append(out(operand))

                case 6:
                    register_b = adv(register_a, operand)

                case 7:
                    register_c = adv(register_a, operand)

        out_string = ",".join(map(str, output))

        if out_string in seen:
            print(f"Seen after: {i}")

        seen.add(out_string)
        if out_string == ",".join(map(str, program)):
            break

    return i


@cache
def adv(register_a, operand):
    return register_a // (2 ** combo_map[operand]())


@cache
def bxl(register_b, operand):
    return register_b ^ operand


@cache
def bst(operand):
    return combo_map[operand]() % 8


@cache
def jnz(operand):
    if register_a != 0:
        return operand
    return None


@cache
def bxc(register_b, register_c):
    return register_c ^ register_b


@cache
def out(operand):
    return combo_map[operand]() % 8


# @cache
# def bdv(register_a, operand):
#     return register_a // (2 ** combo_map[operand]())

# @cache
# def cdv(register_a, operand):
#     return register_a // (2 ** combo_map[operand]())


if __name__ == "__main__":
    # answer = solve(Path(data_path, "input.txt"))
    answer = solve(Path(data_path, "example_2.txt"))
    print(f"Problem 2: {answer}")
