import copy
import re
from collections import defaultdict


def parse_stacks(raw_stack):
    stacks = defaultdict(list)
    for row in reversed(raw_stack.split('\n')[:-1]):
        for stack, crate in enumerate(row[1::4], start=1):
            if crate != " ":
                stacks[stack].append(crate)
    return stacks


def parse_moves(raw_moves):
    moves = []
    for line in raw_moves.split('\n'):
        moves.append(tuple(map(int, re.findall(r'\d+', line))))
    return moves


with open('./2022/05/input.txt') as f:
    raw_stack, raw_moves = f.read().split('\n\n')

stacks_p1 = parse_stacks(raw_stack)
stacks_p2 = copy.deepcopy(stacks_p1)
moves = parse_moves(raw_moves)

for move in moves:
    for i in range(move[0]):
        stacks_p1[move[2]].append(stacks_p1[move[1]].pop())

    stacks_p2[move[2]].extend(stacks_p2[move[1]][-move[0]:])
    del stacks_p2[move[1]][-move[0]:]

print("".join([stack[-1] for stack in stacks_p1.values()]),
      "".join([stack[-1] for stack in stacks_p2.values()]))
