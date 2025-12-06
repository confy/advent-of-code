smol = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""


with open("./2025/02/input.txt", "r") as f:
    data = f.read().strip().split(",")

# data = smol.strip().split(",")

data = [tuple(map(int, x.split("-"))) for x in data]

p1 = 0
p2 = 0


def is_repeated_sequence(n, size):
    s = str(n)
    if len(s) % size == 0:
        part = s[:size]
        if part * (len(s) // size) == s and len(s) // size >= 2:
            return True
    return False


for entry in data:
    start, end = entry

    for i in range(start, end + 1):
        s = str(i)
        half = len(s) // 2
        for size in range(len(s) // 2 + 1, 0, -1):
            if len(s) < 2 * size:
                continue
            if is_repeated_sequence(i, size):
                if size == half and len(s) % 2 == 0:
                    p1 += i
                p2 += i
                break

print("Part 1:", p1)
print("Part 2:", p2)
