from copy import deepcopy
from typing import List

def read_lines(path: str):
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [list(line.strip()) for line in lines]
        return lines


def get_next_east(x, y, len_row):
    return 


def get_next_south():
    ...


def print_sea_floor_map(sea_floor_map):
    for line in sea_floor_map:
        print("".join(line))

    print("\n- - -\n")


def solve_1(path: str):
    sea_floor_map = read_lines(path)
    
    step_counter = 0
    while True:
        map_copy = deepcopy(sea_floor_map)
        move_count = 0
        for y, row in enumerate(sea_floor_map):
            for x, value in enumerate(row):
                
                new_east = (x + 1) % len(row)                
                #if value == "v":
                #    if sea_floor_map[new_south][x] == ".":
                #        map_copy[new_south][x] = "v"
                #        map_copy[y][x] = "."

                if value == ">":
                    if sea_floor_map[y][new_east] == ".":
                        map_copy[y][x] = "."
                        map_copy[y][new_east] = ">"
                        move_count += 1


                        if sea_floor_map[y - 1][x] == "v":
                            map_copy[y - 1][x] = "."
                            map_copy[y][x] = "v"
                            move_count += 1

                elif value == "." and sea_floor_map[y][x - 1] != ">":
                    if sea_floor_map[y - 1][x] == "v":
                        map_copy[y - 1][x] = "."
                        map_copy[y][x] = "v"
                        move_count += 1

        step_counter += 1

        if map_copy == sea_floor_map:
            break

        sea_floor_map = map_copy
        #print_sea_floor_map(sea_floor_map)


        # TODO: REMOVE
        #if step_counter == 5:
        #    break
        
    return step_counter


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
