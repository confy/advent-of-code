smol = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

# lines = smol.strip().split("\n")
left, right = [], []

for line in lines:
    l, r = line.split("   ")
    left.append(int(l))
    right.append(int(r))

def part_1(left, right):
    left.sort()
    right.sort()
    return sum(abs(l - r) for l, r in zip(left, right))

def part_2(left, right):
    r_counts = {r: right.count(r) for r in right}
    return sum(l * r_counts.get(l, 0) for l in left)

print(part_1(left, right))
print(part_2(left, right))
