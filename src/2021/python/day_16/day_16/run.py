import math
from dataclasses import dataclass
from functools import reduce
from typing import Callable, List, Union

def read_line(path: str):
    with open(path, "r") as f:
        return f.read().strip()


@dataclass
class Packet:
    version: int
    type_id: int


@dataclass
class LiteralValue(Packet):
    value: int


@dataclass
class Operator(Packet):
    length_type_id: int
    sub_packets: List[Union["Operator", LiteralValue]]
    operation: Callable


binary_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def hex_to_bin(packet: List[str]) -> List[str]:
    return "".join(binary_map[_hex] for _hex in packet)


def read_packet(bit_stream: List[str], cursor: int = 0):
    type_id = int(bit_stream[cursor + 3:cursor + 6], 2)

    if type_id == 4:
        # Literal value
        packet, cursor = parse_literal_value(bit_stream, cursor)

    else:
        # Operator
        packet, cursor = parse_operator(bit_stream, cursor)

    return packet, cursor
                

def parse_header(bit_stream: List[str], cursor):
    version = int(bit_stream[cursor:(cursor := cursor + 3)], 2)
    type_id = int(bit_stream[cursor:(cursor := cursor + 3)], 2)
    return version, type_id, cursor


def pad_cursor(cursor: int) -> int:
    while cursor % 4 != 0:
        print("Padding")
        cursor += 1
    return cursor


def parse_literal_value(bit_stream: List[str], cursor):
    version, type_id, cursor = parse_header(bit_stream, cursor)

    byte_string = ""
    while (byte := bit_stream[cursor:cursor + 5])[0] == "1":
        byte_string += byte[1:]
        cursor += 5
    else:
        byte_string += bit_stream[cursor + 1: (cursor := cursor + 5)]

    value = int(byte_string, 2)
    packet = LiteralValue(version, type_id, value)

    #cursor = pad_cursor(cursor)

    return packet, cursor

def parse_operator(bit_stream: List[str], cursor):
    version, type_id, cursor = parse_header(bit_stream, cursor)

    if type_id == 0:
        operation = lambda x, y: x + y
    elif type_id == 1:
        operation = lambda x, y: x * y
    elif type_id == 2:
        operation = lambda x, y: x if x < y else y
    elif type_id == 3:
        operation = lambda x, y: x if x > y else y
    elif type_id == 5:
        operation = lambda x, y: int(x > y)
    elif type_id == 6:
        operation = lambda x, y: int(x < y)
    elif type_id == 7:
        operation = lambda x, y: int(x == y)


    length_type_id = int(bit_stream[cursor], 2)
    cursor += 1

    sub_packets = []
    if length_type_id == 0:
        # Total length == next 15 bits
        total_length = int(bit_stream[cursor:(cursor := cursor + 15)], 2)
        target = cursor + total_length
        while cursor < target:
            sub_packet, cursor = read_packet(bit_stream, cursor)
            sub_packets.append(sub_packet)

    elif length_type_id == 1:
        # num_sub_packets == next 11 bits
        num_sub_packets = int(bit_stream[cursor:(cursor := cursor + 11)], 2)
        for _ in range(num_sub_packets):
            sub_packet, cursor = read_packet(bit_stream, cursor)
            sub_packets.append(sub_packet)

    #cursor = pad_cursor(cursor)
    packet = Operator(version, type_id, length_type_id, sub_packets, operation)
    return packet, cursor


def unpack_sub_packets(packet: Operator):
    sub_packets = []
    to_unpack = [*packet.sub_packets]
    while to_unpack:
        packet = to_unpack.pop()
        sub_packets.append(packet)
        if packet.type_id != 4:
            to_unpack += [*packet.sub_packets]
    return sub_packets


def solve_1(data):
    bit_stream = hex_to_bin(data)
    packet, _ = read_packet(bit_stream)

    all_packets = [packet, *unpack_sub_packets(packet)]
    return sum(packet.version for packet in all_packets)


def perform_operation(packet):
    if isinstance(packet, LiteralValue):
        print(packet.value)
        return packet.value
    
    else:
        sub_packet_values = [perform_operation(sub_packet) for sub_packet in packet.sub_packets]
        res = reduce(packet.operation, sub_packet_values)
        return res


def solve_2(data):
    bit_stream = hex_to_bin(data)
    packet, _ = read_packet(bit_stream)
    return perform_operation(packet)


if __name__ == "__main__":
    path = "example.txt"
    example_data = read_line(path)
    ans_1_example = solve_1(example_data)    
    ans_2_example = solve_2(example_data)

    path = "input.txt"
    input_data = read_line(path)
    ans_1_input = solve_1(input_data)
    ans_2_input = solve_2(input_data)
    
    print(f"Example 1: {ans_1_example}")
    print(f"Example 2: {ans_2_example}")
    print("\n- - -\n")
    print(f"Problem 1: {ans_1_input}")
    print(f"Problem 2: {ans_2_input}")
