with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]


smol = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

# lines = smol.strip().split("\n")

position = 50
p1 = 0
p2 = 0

for line in lines:
    direction = line[0]
    steps = int(line[1:])
    for _ in range(steps):
        if direction == "L":
            position = (position - 1) % 100
        else:
            position = (position + 1) % 100
        if position == 0:
            p2 += 1
        print(position)
    if position == 0:
        p1 += 1

print(p1, p2)
