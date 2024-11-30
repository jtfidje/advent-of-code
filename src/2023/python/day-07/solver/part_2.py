from collections import Counter, OrderedDict

from pathlib import Path

from solver import utils

data_path = Path(__file__).parent.parent.absolute() / "data"


def calc_score(count, multiplier):
    return sum(map(lambda x: x[0] * (x[1] * multiplier), count))


def rank_hand(hand):
    best = 0
    if 1 in hand:
        for i in range(2, 15):
            res = rank_hand(tuple([i if j == 1 else j for j in hand]))
            best = max(best, res)
        return best

    hand_count = OrderedDict(sorted(Counter(hand).items(), reverse=True))
    count = list(OrderedDict(sorted(hand_count.items(), key=lambda x: x[1], reverse=True)).items())
    # High card
    if len(hand_count) == 5:
        return 1
    
    # Pair
    elif len(hand_count) == 4:
        return 2
    
    # Two pairs and three of a kind
    elif len(hand_count) == 3:
        if count[0][1] == 3:
            # Three of a kind
            return 4
        
        # Two pairs
        return 3
    
    # Four of a kind and full house
    elif len(hand_count) == 2:
        if count[0][1] == 4:
            # Four of a kind:
            return 6
        
        # Full house
        return 5

    # 5 of a kind
    else:
        return 7
    




def solve(path: str):
    data = utils.read_lines(path)
    data = [line.split() for line in data]

    for line in data:
        line[0] = "-".join(list(line[0]))
        line[0] = line[0].replace("T", "10").replace("J", "1").replace("Q", "12").replace("K", "13").replace("A", "14")
        line[0] = tuple(map(int, line[0].split("-")))

    data = sorted(data, key=lambda x: rank_hand(x[0]))

    hand_map = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
    }

    for hand in data:
        hand_map[rank_hand(hand[0])].append(hand)

    results = []
    for hands in hand_map.values():
        hands = sorted(hands, key=lambda x: x[0], reverse=False)
        results.extend(hands)

    return sum([i * int(line[1]) for i, line in enumerate(results, start=1)])

if __name__ == "__main__":
    answer = solve(Path(data_path, "input.txt"))
    print(f"Problem 2: {answer}")