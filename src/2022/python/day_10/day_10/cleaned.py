
def read_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


class CPU:
    def __init__(self):
        self.registers = {"x": 1}
        self.current_operation = None
        self.operations = []
        self.signal_strength = 0
        self.cycle = 0
        self.crt = ""

    @property
    def sprite(self) -> list[int]:
        return (
            self.registers["x"] - 1,
            self.registers["x"],
            self.registers["x"] + 1
        )

    def load(self, path: str):
        data = read_lines(path)
        for line in data:
            if line == "noop":
                self.operations.append({"type": "noop", "value": 0, "cycles": 1})
            else:
                op, value = line.split()
                value = int(value)
                self.operations.append({"type": op, "value": value, "cycles": 2})

    def tick(self) -> None:
        self.cycle += 1

        if self.current_operation is None:
            try:
                self.current_operation = self.operations.pop(0)
            except IndexError:
                return
        
        self.current_operation["cycles"] -= 1

    def update_signal_strength(self) -> None:
        if (self.cycle == 20 or (self.cycle - 20) % 40 == 0):
            self.signal_strength += self.cycle * self.registers["x"]

    def update_current_operation(self) -> None:
        if self.current_operation["cycles"] == 0:
            self.registers["x"] += self.current_operation["value"]
            self.current_operation = None

    def update_crt(self) -> None:
        cursor = self.cycle % 40
        
        if cursor in self.sprite:
            self.crt += "#"
        else:
            self.crt += "."

        if (self.cycle + 1) % 40 == 0:
            self.crt += "\n"

    def run(self):
        while self.operations or self.current_operation is not None:
            self.update_crt()
            self.tick()
            self.update_signal_strength()
            self.update_current_operation()


def solve_1(path: str) -> str:
    cpu = CPU()
    cpu.load(path)
    cpu.run()

    return cpu.signal_strength

def solve_2(path: str) -> str:
    cpu = CPU()
    cpu.load(path)
    cpu.run()

    return cpu.crt


if __name__ == "__main__":
    crt = solve_2("input.txt")
    crt = crt.replace(".", " ").replace("#", "█")


    print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: \n{solve_2('example.txt')}\n")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: \n\n{crt}")
