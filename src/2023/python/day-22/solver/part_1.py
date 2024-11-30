from collections import defaultdict
from typing import TypeAlias, Self, Literal
from pathlib import Path
from rich import print

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


Point: TypeAlias = "tuple[int, int, int]"

colors = [
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "bright_red",
    "bright_green",
    "bright_yellow",
    "bright_blue",
    "bright_magenta",
    "bright_cyan",
    "bright_white",
]


class Brick:
    def __init__(self, label: int, bounds: tuple[Point, Point]):
        self.label = label
        self.color = colors[label % len(colors)]
        self.bounds = bounds
        self.supports: list[Self] = []
        self.is_critical = False
        self.bricks_above: set[Self] = set()
        self.bricks_below: set[Self] = set()

        self.points = self._calculate_points()
        
    def _calculate_points(self) -> list[Point]:
        x, y, z = self.bounds[0]
        a, b, c = self.bounds[1]
        points = []
        for i in range(x, a + 1):
            for j in range(y, b + 1):
                for k in range(z, c + 1):
                    points.append((i, j, k))
        return points

    def add_brick_below(self, brick: Self):
        self.bricks_below.add(brick)

    def add_brick_above(self, brick: Self):
        self.bricks_above.add(brick.label)

    def shift_down(self):
        x, y, z = self.bounds[0]
        a, b, c = self.bounds[1]
        
        self.bounds = (
            (x, y, z - 1),
            (a, b, c - 1)
        )

        self.points = self._calculate_points()

    def __repr__(self) -> str:
        lower, higher = self.bounds
        return f"{self.label}<{lower}:{higher}>"
    
    def __hash__(self):
        return hash(self.label)
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Brick):
            return False
        return self.label == __value.label


class Field:
    def __init__(self) -> None:
        self.space: dict[Point, Brick] = {}

    @property
    def bricks(self) -> list[Brick]:
        return list(set(self.space.values()))

    def add_brick(self, brick: Brick):
        for point in brick.points:
            self.space[point] = brick

    def remove_brick(self, brick: Brick):
        for point in brick.points:
            self.space.pop(point, None)

    def settle(self):
        _failsafe = 0
        run = True
        while run:
            if _failsafe >= 10_000:
                print("ERROR! Hit failsafe in settle()")
                break

            run = False

            for brick in self.bricks:
                # Remove all points from space
                self.remove_brick(brick)

                # Check to see if all spaces beneath the brick are vacant
                for x, y, z in brick.points:
                    if z <= 1:
                        break

                    if self.space.get((x, y, z - 1)) is not None:
                        break
                else:
                    # All vacant! Move the brick down one space
                    brick.shift_down()
                    run = True  # Continue loop

                # Add brick back into space
                self.add_brick(brick)
            
            _failsafe += 1

    def print_space(self, face: Literal["x", "y", "z"] = "x", use_label: bool=False):
        """Prints the space with the perspective of looking at [face]"""
        max_x = max(p[0] for p in self.space)
        max_y = max(p[1] for p in self.space)
        max_row = max([max_x, max_y])

        if face == "x":
            max_row = max_x
        elif face == "y":
            max_row = max_y

        if face == "z":
            # Create a point-map keyed by y-value
            point_map = defaultdict(list)
            for x, y, z in self.space:
                point_map[y].append((x, z))
            max_col = max(point_map)
        else:
            # Create a point-map keyed by z-value
            point_map = defaultdict(list)
            for x, y, z in self.space:
                point_map[z].append((x, y))
            max_col = max(point_map)
        
        # Print face header
        row = [" "] * max_row
        row[int(max_row / 2)] = "x" if face == "z" else face
        print("".join(row))
        print("".join(str(i) for i in range(max_row + 1)))
        print()

        cache = {}
        # Print the brick space from the top down
        _range = range(max_col, 0, -1)

        for i in _range:
            row = ["[grey27].[/grey27]"] * (max_row + 1)
            for point in point_map[i]:
                if face == "z":
                    x, z = point
                    y = i
                else:
                    x, y = point
                    z = i

                brick = self.space[(x, y, z)]

                if face == "x":
                    k = x
                elif face == "y":
                    k = y
                elif face == "z":
                    k = x
                
                if (c := cache.get((k, i))) is None or c == brick.label:
                    cache[(k, i)] = brick.label
                    s = f"[{brick.color}]{brick.label if use_label else '■'}[/{brick.color}]"
                else:
                    s = "[grey35]*[/grey35]"

                row[k] = s
                
            if i == int(len(_range) / 2):
                print("".join(row), i, "y" if face == "z" else "z")
            else:
                print("".join(row), i)
            
        print("-" * (max_row + 1), 0)


def solve(path: str):
    data = utils.read_lines(path)

    # Perform this step to sort all the brick-positions first
    # Should make colors better
    brick_lines = []
    for line in data:
        a, b = line.split("~")
        x = tuple(map(int, a.split(",")))
        y = tuple(map(int, b.split(",")))
        brick_lines.append((x, y))
    brick_lines = sorted(brick_lines, key=lambda x: x[0][2])
    
    # Create brick-field
    field = Field()
    for label, line in enumerate(brick_lines, start=1):
        x, y, z = line[0]
        a, b, c = line[1]
        
        brick = Brick(
            label=label,
            bounds=((x, y, z), (a, b, c))
        )
        field.add_brick(brick)

    field.settle()
    #field.print_space(face="x", use_label=False)
    #field.print_space(face="y", use_label=False)
    #field.print_space(face="z", use_label=False)
    


    can_be_removed = set()
    for brick in field.bricks:
        for x, y, z in brick.points:
            p_above = (x, y, z + 1)
            b_above = field.space.get(p_above)
            if b_above is not None and b_above.label != brick.label:
                brick.add_brick_above(b_above)

            if z <= 1:
                continue

            p_below = (x, y, z - 1)
            b_below = field.space.get(p_below)
            if b_below is not None and b_below.label != brick.label:
                brick.add_brick_below(b_below)
                
        if not brick.bricks_above:
            can_be_removed.add(brick.label)
        
        # Mark critical
        if len(brick.bricks_below) == 1:
            for b_below in brick.bricks_below:
                b_below.is_critical = True

    for brick in field.bricks:
        if len(brick.bricks_below) >= 2:
            for b_below in brick.bricks_below:
                if not b_below.is_critical:
                    can_be_removed.add(b_below.label) 

    return len(can_be_removed)


if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    #answer = solve(Path(data_path, "example_1.txt"))
    #answer = solve(Path(data_path, "example_1_2.txt"))
    print(f"Problem 1: {answer}")


    # TOO HIGH:  633
    # TOO HIGH: 1023