with open("./2023/09/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]


smol = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

# lines = smol.split("\n")


def get_diff(values):
    while True:
        cur = values[-1]
        new = [cur[i + 1] - cur[i] for i in range(len(cur) - 1)]
        values.append(new)
        if all(number == 0 for number in new):
            return values


def get_new_values(values: list):
    values[-1].append(0)
    values[-1].insert(0, 0)
    for i in range(len(values) - 2, -1, -1):
        values[i].append(values[i][-1] + values[i + 1][-1])
        values[i].insert(0, values[i][0] - values[i + 1][0])
    return values


p1 = 0
p2 = 0

for row in lines:
    history = [[int(n) for n in row.split()]]
    history = get_diff(history)
    history = get_new_values(history)
    p1 += history[0][-1]
    p2 += history[0][0]

print(p1, p2)
