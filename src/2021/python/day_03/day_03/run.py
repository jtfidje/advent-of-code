from collections import Counter
from typing import List
from copy import copy


def read_lines(path: str) -> List[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def count_bits(data):
    new_arr = []
    for i in range(len(data[0])):
        temp = []
        for line in data:
            temp.append(line[i])
        new_arr.append(temp)
    
    most_common = []
    fewest = []
    for line in new_arr:
        counter = Counter(line)

        if counter["1"] == counter["0"]:
            most_common.append("1")
        elif counter["1"] > counter["0"]:
            most_common.append("1")
        else:
            most_common.append("0")

        if counter["1"] == counter["0"]:
            fewest.append("0")
        elif counter["1"] > counter["0"]:
            fewest.append("0")
        else:
            fewest.append("1")
    return most_common, fewest


def solve_1(path: str) -> int:
    data = read_lines(path)
    new_arr = []
    for i in range(len(data[0])):
        temp = []
        for line in data:
            temp.append(line[i])
        new_arr.append(temp)

    temp_gamma = []
    temp_epsilon = []
    for line in new_arr:
        counter = Counter(line)
        if counter["0"] > counter["1"]:
            temp_gamma.append("0")
            temp_epsilon.append("1")
        else:
            temp_gamma.append("1")
            temp_epsilon.append("0")

    gamma = int("".join(temp_gamma), 2)
    epsilon = int("".join(temp_epsilon), 2)

    return gamma * epsilon


def solve_2(path: str) -> int:
    data = read_lines(path)

    temp = copy(data)
    for i in range(len(data[0])):
        most_common, fewest = count_bits(temp)
        common = most_common[i]
        new_temp = []
        for line in temp:
            if line[i] == common:
                new_temp.append(line)
        temp = copy(new_temp)
        if len(temp) == 1:
            break
    
    oxygen = int("".join(temp), 2)

    temp = copy(data)
    for i in range(len(data[0])):
        most_common, fewest = count_bits(temp)
        common = fewest[i]
        new_temp = []
        for line in temp:
            if line[i] == common:
                new_temp.append(line)
        temp = copy(new_temp)
        if len(temp) == 1:
            break
    
    co2 = int("".join(temp), 2)
    return oxygen * co2


if __name__ == "__main__":
    path = "input.txt"

    ans_1 = solve_1(path)
    print(f"Problem 1: {ans_1}")
    
    ans_2 = solve_2(path)
    print(f"Problem 2: {ans_2}")
