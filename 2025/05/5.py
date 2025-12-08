smol = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def join_ranges(ranges):
    ranges = sorted(ranges)
    merged = []
    for start, end in ranges:
        if not merged or merged[-1][1] < start - 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return [tuple(r) for r in merged]


p1 = p2 = 0

with open("./2025/05/input.txt", "r") as f:
    data = f.read().strip()

# data = smol

ranges, ingredients = data.split("\n\n")
ranges = [tuple(map(int, r.split("-"))) for r in ranges.splitlines()]
ingredients = [int(b) for b in ingredients.splitlines()]

ranges = join_ranges(ranges)


for n in ingredients:
    for start, end in ranges:
        if start <= n <= end:
            p1 += 1
            break

for start, end in ranges:
    p2 += end - start + 1

print("Part 1:", p1)
print("Part 2:", p2)
