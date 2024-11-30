from typing import List, Tuple

class SubmarineOne:
    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0

    def _move_forward(self, value: int) -> None:
        self.horizontal_position += value

    def _change_depth(self, value: int) -> None:
        self.depth += value

    def get_result(self) -> int:
        return self.horizontal_position * self.depth

    def read_command(self, command: str, value: int) -> None:
        if command == "forward":
            self._move_forward(value)
        elif command == "down":
            self._change_depth(value)
        elif command == "up":
            self._change_depth(-value)
        else:
            print(f"Unknown command '{command}'. Ignoring...")


class SubmarineTwo(SubmarineOne):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def _move_forward(self, value: int) -> None:
        self.horizontal_position += value
        self.depth += self.aim * value

    def _change_depth(self, value: int) -> None:
        self.aim += value


def read_commands(path: str) -> List[Tuple[str, int]]:
    with open(path, "r") as f:
        lines = f.readlines()

    commands = []
    for line in lines:
        command, value = line.strip().split(" ")
        commands.append((command, int(value)))

    return commands


def solve_1(path: str) -> int:
    commands = read_commands(path)
    submarine = SubmarineOne()

    for command, value in commands:
        submarine.read_command(command, value)

    return submarine.get_result()


def solve_2(path: str) -> int:
    commands = read_commands(path)
    submarine = SubmarineTwo()

    for command, value in commands:
        submarine.read_command(command, value)

    return submarine.get_result()


if __name__ == "__main__":
    path = "input.txt"

    ans_1 = solve_1(path)
    print(f"The final horizontal position multiplied by the final depth is: {ans_1}")
    
    ans_2 = solve_2(path)
    print(f"The final horizontal position multiplied by the final depth is: {ans_2}")