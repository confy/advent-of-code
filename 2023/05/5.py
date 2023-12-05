with open('./2023/05/input.txt') as f:
    data = f.read()

smol = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

parts = data.split("\n\n")
seeds = [int(x) for x in parts[0].split(":")[1].split()]
maps = [[[int(x) for x in s.split()] for s in parts[i].split("\n")[1:]] for i in range(1, len(parts))]

ranges = [(seeds[i], seeds[i+1]+seeds[i]-1) for i in range(0, len(seeds), 2)]

for m in maps:
    new_ranges = []
    for j in range(len(m)):
        start = m[j][1]
        end = m[j][1] + map[j][2] - 1
        cut_ranges = []
        for r in ranges:
            if end >= r[0] and start <= r[1]:
                c1 = max(start, r[0])
                c2 = min(end, r[1])
                new_ranges.append(
                    (c1 + m[j][0] - m[j][1], c2 + m[j][0] - m[j][1]))
                if r[0] < c1:
                    cut_ranges.append((r[0], c1-1))
                if r[1] > c2:
                    cut_ranges.append((c2+1, r[1]))
            else:
                cut_ranges.append(r)
        ranges = cut_ranges
    ranges = cut_ranges + new_ranges
    print(min(r[0] for r in ranges))
