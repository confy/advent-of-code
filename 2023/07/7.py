import enum
from collections import Counter
with open('./2023/07/input.txt')as f:
    lines = [line.strip() for line in f.readlines()]

smol = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

# lines = smol.split('\n')


class Hand(enum.Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


def parse_input(lines: list):
    hands = []
    for line in lines:
        hand, score = line.split()
        score = int(score)
        hands.append((hand, score))
    return hands


def get_hand(hand: str, with_jokers: bool):
    counts = Counter(hand)
    if with_jokers:
        num_jokers = counts["J"]
        counts["J"] = 0
        if not counts:
            counts["A"] = 5
            mc = "A"
        else:
            mc, _ = counts.most_common()[0]
            counts[mc] += num_jokers
        hand = hand.replace("J", mc)

    match max(counts.values()):
        case 5:
            hand_val = Hand.FIVE_OF_A_KIND
        case 4:
            hand_val = Hand.FOUR_OF_A_KIND
        case 3:
            hand_val = Hand.FULL_HOUSE if 2 in counts.values() else Hand.THREE_OF_A_KIND
        case 2:
            hand_val = Hand.TWO_PAIR if list(counts.values()).count(2) == 2 else Hand.PAIR
        case 1:
            hand_val = Hand.HIGH_CARD
    return hand, hand_val


def run(hands: list[tuple], with_jokers: bool):
    cards_in_order = "J23456789TQKA" if with_jokers else "23456789TJQKA"
    hands_with_scores = []
    for hand in hands:
        score = hand[1]
        new_hand, hand_val = get_hand(hand[0], with_jokers)
        hands_with_scores.append((hand[0], new_hand, score, hand_val))

    hands_with_scores.sort(key=lambda x: cards_in_order.index(x[0][4]))
    hands_with_scores.sort(key=lambda x: cards_in_order.index(x[0][3]))
    hands_with_scores.sort(key=lambda x: cards_in_order.index(x[0][2]))
    hands_with_scores.sort(key=lambda x: cards_in_order.index(x[0][1]))
    hands_with_scores.sort(key=lambda x: cards_in_order.index(x[0][0]))
    hands_with_scores.sort(key=lambda x: x[3].value)
    return sum(hand[2] * (i+1) for i, hand in enumerate(hands_with_scores))


hands = parse_input(lines)
print("Part 1:", run(hands, False))
print("Part 2:", run(hands, True))
