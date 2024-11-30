
from typing import List


data = None

def read_lines(path: str):
    with open(path, "r") as f:
        data = f.read().strip()
        data = data.split("area: ")[-1]
        x, y = data.split(", ")
        x = [int(i) for i in x[2:].split("..")]
        y = [int(i) for i in y[2:].split("..")]

        return x, y


def check_state(pos):
    area_x, area_y = data

    # Check if passed
    if area_x[1] < pos[0] or area_y[0] > pos[1]:
        return "failed"

    # Check if inside
    if area_x[0] <= pos[0] <= area_x[1]:
        if area_y[0] <= pos[1] <= area_y[1]:
            return "inside"

    # Still moving towards
    return "moving"

def solve_1(path: str):
    global data
    data = read_lines(path)
    x_pos, y_pos = (0, 0)

    return abs(data[1][0]) * abs(data[1][0] + 1) // 2
    

    max_y = 0
    y_vel = 0
    for init_x_vel in range(data[0][1] // 2):
        for init_y_vel in range(200):
            x_pos, y_pos = (0, 0)
            current_best = 0
            x_vel = init_x_vel
            y_vel = init_y_vel
            while True:
                x_pos += x_vel
                y_pos += y_vel

                current_best = max(current_best, y_pos)

                if x_vel < 0:
                    x_vel += 1
                elif x_vel > 0:
                    x_vel -= 1
                else:
                    ...

                y_vel -= 1

                state = check_state((x_pos, y_pos))
                if state == "moving":
                    continue
                if state == "failed":
                    break
                
                if state == "inside":
                    max_y = max(max_y, current_best)
                    break

    return max_y



def solve_2(path: str):
    global data
    data = read_lines(path)
    x_pos, y_pos = (0, 0)
    
    vector_count = 0
    for init_x_vel in range(data[0][1] + 1):
        for init_y_vel in range(data[1][0], 200):
            x_pos, y_pos = (0, 0)
            current_best = 0
            x_vel = init_x_vel
            y_vel = init_y_vel
            while True:
                x_pos += x_vel
                y_pos += y_vel

                current_best = max(current_best, y_pos)

                if x_vel < 0:
                    x_vel += 1
                elif x_vel > 0:
                    x_vel -= 1
                else:
                    ...

                y_vel -= 1

                state = check_state((x_pos, y_pos))
                if state == "moving":
                    continue
                if state == "failed":
                    break
                
                if state == "inside":
                    vector_count += 1
                    break

    return vector_count


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
