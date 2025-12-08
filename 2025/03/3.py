smol = """987654321111111
811111111111119
234234234234278
818181911112111"""

# smol = """987654321111111"""

with open("./2025/03/input.txt", "r") as f:
    data = [s.strip() for s in f.readlines()]

# data = smol.split("\n")

p1 = p2 = 0


def part1(entry):
    start_digit = int(entry[0])
    start_idx = 0
    end_digit = 0
    for i in range(0, len(entry) - 1):
        if int(entry[i]) > start_digit:
            start_digit = int(entry[i])
            start_idx = i
    for j in range(start_idx + 1, len(entry)):
        if int(entry[j]) > end_digit:
            end_digit = int(entry[j])
    return start_digit * 10 + end_digit


def part2(entry):
    k = 12
    n = len(entry)
    result_digits = []
    start = 0
    for i in range(k):
        end = n - (k - i) + 1
        max_digit = max(entry[start:end])
        idx = entry.index(max_digit, start, end)
        result_digits.append(max_digit)
        start = idx + 1
    digits = "".join(result_digits)
    return int(digits)


for entry in data:
    p1 += part1(entry)
    p2 += part2(entry)


print("Part 1:", p1)
print("Part 2:", p2)
