# flake8: noqa: F401

from collections import defaultdict
import math
import re
from pathlib import Path
from typing import Self

from advent_of_code import utils
from aoc_2025_10 import DATA_PATH


class Node:
    def __init__(
        self, press_id: int, state: dict[int, int], parent: None | Self = None
    ):
        self.press_id = press_id
        self.state = state
        self.state_tuple = tuple(self.state[i] for i in range(len(self.state)))
        self.parent = parent

    def get_state_path(self) -> list[tuple[int, tuple[int, ...]]]:
        node = self
        states = [(node.press_id, node.state_tuple)]
        while node.parent:
            node = node.parent
            states.append((node.press_id, node.state_tuple))
        return states

    def __repr__(self) -> str:
        return f"<Node {self.press_id} {self.state_tuple}>"


@utils.performance_timer
def solve(path: str | Path):
    data = utils.read_lines(path)

    result = 0
    for line in data:
        _, buttons, joltage = re.findall(r"\[([\.#]+)\] (\(.*\)) (\{[\d,]+\})", line)[0]

        target = {i: x for i, x in enumerate(utils.parse_integers(joltage))}
        buttons = sorted(
            list(map(utils.parse_integers, buttons.split(" "))),
            reverse=False,
            key=lambda x: len(x),
        )

        state = {key: 0 for key in target}
        press_id = 0

        # while True:
        #     break_ = True
        #     index_map = defaultdict(set)
        #     for i, button in enumerate(buttons):
        #         for ix in button:
        #             index_map[ix].add(i)

        #     to_remove = []
        #     for ti, bid in index_map.items():
        #         if len(bid) == 1:
        #             break_ = False
        #             [bi] = bid
        #             press_id += target[ti]
        #             for i in buttons[bi]:
        #                 state[i] += target[ti]
        #             to_remove.append(bi)

        #     if break_:
        #         break

        #     buttons = [b for i, b in enumerate(buttons) if i not in to_remove]

        buttons.sort(key=lambda b: len(b), reverse=True)

        best = math.inf
        visited: dict[tuple[int, ...], int] = {}
        to_visit = [Node(press_id=press_id, state=state)]
        while to_visit:
            to_visit.sort(
                key=lambda n: sum(target[i] - n.state[i] for i in target.keys())
            )

            node = to_visit.pop(0)

            if node.state == target:
                best = min(node.press_id, best)
                to_visit = [n for n in to_visit if n.press_id < best]
                for press_id, state in node.get_state_path():
                    visited[state] = press_id

                print(best, node.press_id)
                continue

            if node.press_id + 1 >= best:
                continue

            for button in buttons:
                if any(node.state[i] == target[i] for i in button):
                    continue

                new_state = {key: value for key, value in node.state.items()}
                for i in button:
                    new_state[i] += 1

                new_node = Node(
                    press_id=node.press_id + 1, state=new_state, parent=node
                )

                if new_node.state_tuple in visited:
                    if new_node.press_id >= visited[new_node.state_tuple]:
                        continue
                    else:
                        del visited[new_node.state_tuple]

                i, n = next(
                    (
                        (i, n)
                        for i, n in enumerate(to_visit)
                        if n.state_tuple == new_node.state_tuple
                    ),
                    (0, None),
                )

                if n is not None:
                    if new_node.press_id < n.press_id:
                        to_visit.pop(i)
                    else:
                        continue

                to_visit.append(new_node)

        result += best

    return result


if __name__ == "__main__":
    answer = solve(DATA_PATH / "example_1_1.txt")
    # answer = solve(DATA_PATH / "input.txt")
    if answer is not None:
        print(f"Problem 2: {answer}")
