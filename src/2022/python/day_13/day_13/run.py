import json
from functools import reduce
from typing import Any
from functools import cmp_to_key

def json_print(obj: dict | list) -> None:
    print(json.dumps(obj, indent=4))


def read_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return lines


def read_data(path: str) -> list[str]:
    pairs = []
    with open(path, "r") as f:
        data = f.read().strip()
        data = data.split("\n\n")
        for pair in data:
            pair = pair.strip().split("\n")
            pairs.append([
                json.loads(pair[0]),
                json.loads(pair[1])
            ])

        return pairs

def read_packets(path: str) -> list[str]:
    packets = []
    with open(path) as f:
        data = f.read().strip().replace("\n\n", "\n")
        for packet in data.split("\n"):
            packet.strip()
            packets.append(json.loads(packet))
    return packets


def read_numbers(path: str) -> list[int]:
    with open(path, "r") as f:
        lines = [line for line in f.readlines()]
        lines = [line.strip() for line in lines]
        return list(map(int, lines))


def compare(left, right):
    left = left.copy()
    right = right.copy()
    while True:
        if left == [] and right == []:
            return 0
        try:
            l = left.pop(0)
        except IndexError:
            return 1

        try:
            r = right.pop(0)
        except IndexError:
            return -1
        
        if all([isinstance(l, int), isinstance(r, int)]):
            if l > r:
                return -1

            elif l < r:
                return 1
            
            else: 
                continue
        
        elif all([isinstance(l, list), isinstance(r, list)]):
            res = compare(l, r)
            if res == 0:
                continue
            return res
        
        else:
            if isinstance(l, int):
                l = [l]
            else:
                r = [r]
            
            res = compare(l, r)
            if res == 0:
                continue
            return res


def solve_1(path: str) -> Any:
    pairs = read_data(path)
    indices = []
    for i, (left, right) in enumerate(pairs, start=1):

        _cmp = compare(left, right)
        if _cmp == 1:
            indices.append(i)
    return sum(indices)
                

def packet_string(packet):
    if packet == []:
        return "0"
    
    string = ""

    for value in packet:
        if isinstance(value, list):
            s = packet_string(value)
        else:
            s = str(value)

        string += s
            
    return string



def solve_2(path: str) -> Any:
    packets = read_packets(path)
    packets.extend([[[2]], [[6]]])

    packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
    i_1 = packets.index([[2]])
    i_2 = packets.index([[6]])
    return (i_1 + 1) * (i_2 + 1)
    
if __name__ == "__main__":
    print(f"Example 1: {solve_1('example.txt')}")
    print(f"Example 2: {solve_2('example.txt')}")
    print("\n- - -\n")
    print(f"Problem 1: {solve_1('input.txt')}")
    print(f"Problem 2: {solve_2('input.txt')}")
