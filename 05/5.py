from collections import defaultdict


def read_input(filename):
    with open("./05/input.txt") as f:
        lines = [i.strip() for i in f.readlines()]
    segs = []
    for line in lines:
        p1, p2 = line.split(" -> ")
        x1, y1 = p1.split(",")
        x2, y2 = p2.split(",")
        segs.append([int(n) for n in [x1, y1, x2, y2]])
    return segs


def myrange(x1, y1, x2, y2):
    while True:
        yield(x1, y1)
        if x1 == x2 and y1 == y2:
            return
        if x1 != x2:
            x1 += (1 if x1 <= x2 else -1)
        if y1 != y2:
            y1 += (1 if y1 <= y2 else -1)


if __name__ == '__main__':
    segs = read_input('./05/input.txt')
    points = defaultdict(lambda: 0)
    for seg in segs:
        # uncomment for part 1
        # if seg[0] == seg[2] or seg[1] == seg[3]:
        for xr, yr in myrange(seg[0], seg[1], seg[2], seg[3]):
            points[(xr, yr)] += 1

    overlaps = sum(hits > 1 for point, hits in points.items())

    print(overlaps)
