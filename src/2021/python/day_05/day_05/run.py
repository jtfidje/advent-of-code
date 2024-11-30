from collections import Counter
from collections import defaultdict
from typing import List

def read_lines(path: str) -> List[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def solve_1(path: str) -> int:
    data = read_lines(path)
    point_pairs = [d.split(" -> ") for d in data]
    
    _map = defaultdict(int)

    for point_pair in point_pairs:
        p1 = point_pair[0].split(",")
        p1 = (int(p1[0]), int(p1[1]))

        p2 = point_pair[1].split(",")
        p2 = (int(p2[0]), int(p2[1]))


        if not (p1[0] == p2[0] or p1[1] == p2[1]):
            continue

        if p1[0] <= p2[0]:
            i_0 = p1[0]
            i_1 = p2[0] + 1
            i_s = 1
        elif p1[0] >= p2[0]:
            i_0 = p1[0]
            i_1 = p2[0] - 1
            i_s = -1
        else:
            i_0 = p1[0]
            i_1 = p2[0] + 1
            i_s = 1

        if p1[1] <= p2[1]:
            j_0 = p1[1]
            j_1 = p2[1] + 1
            j_s = 1
        elif p1[1] > p2[1]:

            j_0 = p1[1]
            j_1 = p2[1] - 1
            j_s = -1
        else:
            j_0 = p1[1]
            j_1 = p2[1] + 1
            j_s = 1

        for i in range(i_0, i_1, i_s):
            for j in range(j_0, j_1, j_s):
                point = (i, j)
                _map[point] += 1

    res = Counter(_map.values())
    res = sum(val for key, val in res.items() if key >= 2)
    return res




def solve_2(path: str) -> int:
    data = read_lines(path)
    point_pairs = [d.split(" -> ") for d in data]
    
    _map = defaultdict(int)

    for point_pair in point_pairs:
        p1 = point_pair[0].split(",")
        p1 = (int(p1[0]), int(p1[1]))

        p2 = point_pair[1].split(",")
        p2 = (int(p2[0]), int(p2[1]))

        if p1[0] <= p2[0]:
            i_0 = p1[0]
            i_1 = p2[0] + 1
            i_s = 1
        elif p1[0] >= p2[0]:
            i_0 = p1[0]
            i_1 = p2[0] - 1
            i_s = -1
        else:
            i_0 = p1[0]
            i_1 = p2[0] + 1
            i_s = 1

        if p1[1] <= p2[1]:
            j_0 = p1[1]
            j_1 = p2[1] + 1
            j_s = 1
        elif p1[1] > p2[1]:

            j_0 = p1[1]
            j_1 = p2[1] - 1
            j_s = -1
        else:
            j_0 = p1[1]
            j_1 = p2[1] + 1
            j_s = 1

        if (p1[0] != p2[0]) and (p1[1] != p2[1]):
            for i in range(i_0, i_1, i_s):
                point = (i, j_0)
                _map[point] += 1
                j_0 += j_s
        else:
            for i in range(i_0, i_1, i_s):
                for j in range(j_0, j_1, j_s):
                    point = (i, j)
                    _map[point] += 1

    res = Counter(_map.values())
    res = sum(val for key, val in res.items() if key >= 2)
    return res


if __name__ == "__main__":
    path = "example.txt"
    ans_1_e = solve_1(path)    
    ans_2_e = solve_2(path)

    path = "input.txt"
    ans_1_s = solve_1(path)
    ans_2_s = solve_2(path)
    
    print(f"Example 1: {ans_1_e}")
    print(f"Example 2: {ans_2_e}")
    print("- - -")
    print(f"Problem 1: {ans_1_s}")
    print(f"Problem 2: {ans_2_s}")
