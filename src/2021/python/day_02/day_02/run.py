from typing import List

def read_lines(path: str) -> List[str]:
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]


def solve_1(path: str) -> int:
    data = read_lines(path)
    x, y = 0, 0

    for line in data:
        cmd, z = line.split(" ")
        z = int(z)

        if cmd == "forward":
            x += z
        elif cmd == "down":
            y += z
        elif cmd == "up":
            y -= z
    return x * y


def solve_2(path: str) -> int:
    data = read_lines(path)
    x, y, aim = 0, 0, 0

    for line in data:
        cmd, z = line.split(" ")
        z = int(z)

        if cmd == "forward":
            x += z
            y += (aim * z)
        elif cmd == "down":
            aim += z
        elif cmd == "up":
            aim -= z

    return x * y



if __name__ == "__main__":
    path = "input.txt"

    ans_1 = solve_1(path)
    print(f"The final horizontal position multiplied by the final depth is: {ans_1}")
    
    ans_2 = solve_2(path)
    print(f"The final horizontal position multiplied by the final depth is: {ans_2}")