# flake8: noqa: F401
from typing import Self
from copy import deepcopy
from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


class Light:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self):
        match self.direction:
            case "up":
                self.position = (
                    self.position[0] + -1,
                    self.position[1] + 0
                )

            case "down":
                self.position = (
                    self.position[0] + 1,
                    self.position[1] + 0
                )

            case "left":
                self.position = (
                    self.position[0] + 0,
                    self.position[1] + -1
                )

            case "right":
                self.position = (
                    self.position[0] + 0,
                    self.position[1] + 1
                )

    def __repr__(self):
        return f"Light {self.position} {self.direction}"
    
    def __eq__(self, __value: Self) -> bool:
        self.position == __value.position and self.direction == __value.direction

def solve(path: str):
    data = utils.read_lines(path)

    visited = {}
    to_visit = [Light(position=(0, 0), direction="right")]
    while to_visit:
        light = to_visit.pop(0)

        while not utils.out_of_bounds(*light.position, data) and (light.position, light.direction) not in visited:
            visited[(light.position, light.direction)] = True

            row, col = light.position
            match data[row][col]:
                case "\\":
                    match light.direction:
                        case "up":
                            light.direction = "left"
                        case "down":
                            light.direction = "right"
                        case "left":
                            light.direction = "up"
                        case "right":
                            light.direction = "down"

                case "/":
                    match light.direction:
                        case "up":
                            light.direction = "right"
                        case "down":
                            light.direction = "left"
                        case "left":
                            light.direction = "down"
                        case "right":
                            light.direction = "up"

                case "|":
                    if light.direction in ["left", "right"]:
                        new_light = Light(position=light.position, direction="up")
                        new_light.move()

                        if (new_light.position, new_light.direction) not in visited and light not in to_visit:
                            to_visit.append(new_light)

                        light.direction = "down"

                case "-":
                    if light.direction in ["up", "down"]:
                        new_light = Light(position=light.position, direction="left")
                        new_light.move()
                        
                        if (new_light.position, new_light.direction) not in visited and light not in to_visit:
                            to_visit.append(new_light)

                        light.direction = "right"

            light.move()

    return len(set(element[0] for element in visited))


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 1: {answer}")