from copy import deepcopy
from typing import List
from collections import namedtuple


energy_map = {
    "amber": 1,
    "bronze": 10,
    "copper": 100,
    "desert": 1000
}

class Amphipod:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __repr__(self):
        return self.name

class Amber(Amphipod):
    cost = 1
    home = 3

class Bronze(Amphipod):
    cost = 10
    home = 5

class Copper(Amphipod):
    cost = 100
    home = 7

class Desert(Amphipod):
    cost = 1000
    home = 9


class Room:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.occupant = None

    @property
    def is_safe(self):
        # A room is safe if it is not outside one of the amphipod-rooms
        return "h" in self.name

    @property
    def is_valid(self):
        # A room is valid if it is not already occupied 
        return self.occupant is None

    def __repr__(self):
        return self.name

def read_map(path: str):
    a_counter = iter(range(1, 3))
    b_counter = iter(range(1, 3))
    c_counter = iter(range(1, 3))
    d_counter = iter(range(1, 3))
    with open(path, "r") as f:
        data = f.read()
        data = data.replace("  ", "")
        grid = [list(line) for line in data.split("\n")]

        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == "A":
                    pod = Amber(f"A{next(a_counter)}", [i, j])
                elif value == "B":
                    pod = Amber(f"B{next(b_counter)}", [i, j])
                elif value == "C":
                    pod = Amber(f"C{next(c_counter)}", [i, j])
                elif value == "D":
                    pod = Amber(f"D{next(d_counter)}", [i, j])
                else:
                    continue
                
                grid[i][j] = pod

            while len(grid[i]) != 13:
                grid[i] = ["#", *grid[i], "#"]

        return grid



def read_lines(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]

        rooms = create_room_map()
        
        temp = [
            [
                lines[2][3],
                lines[2][5],
                lines[2][7],
                lines[2][9],
            ],
            [
                lines[3][3],
                lines[3][5],
                lines[3][7],
                lines[3][9],
            ],
        ]

        amphipods = []
        for level, arr in enumerate(temp):
            for amphipod, room_letter in zip(arr, ["a", "b", "c", "d"]):
                if amphipod == "A":
                    room = rooms[f"{room_letter}{level}"]
                    amphipod = Amber(f"A{level}", room.name)
                    amphipods.append(amphipod)
                    room.occupant = amphipod.name
                elif amphipod == "B":
                    room = rooms[f"{room_letter}{level}"]
                    amphipod = Bronze(f"B{level}", room.name)
                    amphipods.append(amphipod)
                    room.occupant = amphipod.name
                elif amphipod == "C":
                    room = rooms[f"{room_letter}{level}"]
                    amphipod = Copper(f"C{level}", room.name)
                    amphipods.append(amphipod)
                    room.occupant = amphipod.name
                elif amphipod == "D":
                    room = rooms[f"{room_letter}{level}"]
                    amphipod = Desert(f"D{level}", room.name)
                    amphipods.append(amphipod)
                    room.occupant = amphipod.name

        return rooms, amphipods


def create_room_map():
    # Hallway
    rooms = {}
    for i in range(11):
        name = f"h{i}"
        rooms[name] = Room(name=name)

    for i, j in zip(range(0, 10), range(1, 11)):
        rooms[f"h{i}"].right = rooms[f"h{j}"]
        rooms[f"h{j}"].left = rooms[f"h{i}"]

    for x, i in zip(["a", "b", "c", "d"], [2, 4, 6, 8]):
        name_a = f"{x}0"
        name_b = f"{x}1"

        rooms[name_a] = Room(name_a)
        rooms[name_b] = Room(name_b)

        rooms[name_a].up = rooms[f"h{i}"]
        rooms[name_a].down = rooms[name_b]
        rooms[name_b].up = rooms[name_a]

    return rooms


def move(amphipods, rooms):
    amphipod = deepcopy(amphipod)
    rooms = deepcopy(rooms)

    # Find a new, safe room
    for direction in ["up", "down", "left", "right", "skip"]:
        if direction == "skip":
            ...
        new_room = getattr(rooms[amphipod.room], direction)
        if new_room is None or not new_room.is_valid:
            continue


    
        if new_room and new_room.occupied is not None:
            # Room in direction is not occupied
            if not new_room.is_safe:
                for 
    
    amphipod.move(direction)





def solve_1(path: str):
    rooms, amphipods = read_lines(path)
    print(list(rooms.values()))


def solve_2(path: str):
    data = read_lines(path)
    ...


if __name__ == "__main__":
    path = "example.txt"
    ans_1_example = solve_1(path)    
    ans_2_example = solve_2(path)

    path = "input.txt"
    ans_1_input = solve_1(path)
    ans_2_input = solve_2(path)
    
    print(f"Example 1: {ans_1_example}")
    print(f"Example 2: {ans_2_example}")
    print("\n- - -\n")
    print(f"Problem 1: {ans_1_input}")
    print(f"Problem 2: {ans_2_input}")
