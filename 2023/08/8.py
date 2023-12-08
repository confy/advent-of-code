from dataclasses import dataclass
import math

with open("./2023/08/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

smol = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

smol = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

# lines = smol.split('\n')

RL = lines.pop(0)
lines = lines[1:]


@dataclass
class Node:
    name: str
    left: str
    right: str


def parse_input(lines: list):
    nodes = {}
    for line in lines:
        name, lr = line.split(" = ")
        l, r = lr[1:-1].split(", ")
        nodes[name] = Node(name, l, r)
    return nodes


def get_steps_for_condition(nodes, node, condition):
    steps = 0
    while condition(node):
        for direction in RL:
            node = nodes[node.left] if direction == "L" else nodes[node.right]
            steps += 1
            if not condition(node):
                break
    return steps


nodes = parse_input(lines)

# part 1
steps = get_steps_for_condition(nodes, nodes["AAA"], lambda node: node.name != "ZZZ")
print(steps)

# part 2
cur_nodes = [node for node in nodes.values() if node.name[2] == "A"]
node_steps = [
    get_steps_for_condition(nodes, node, lambda node: node.name[2] != "Z")
    for node in cur_nodes
]
print(math.lcm(*node_steps))
