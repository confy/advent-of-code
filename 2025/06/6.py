from math import prod

smol = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +"""

p1 = p2 = 0

with open("./2025/06/input.txt", "r") as f:
    data = f.read()

# data = smol

data = data.splitlines()

ops = data[-1].split()
p1 = sum(
    prod(map(int, nums)) if ops[i] == "*" else sum(map(int, nums))
    for i, nums in enumerate(zip(*[r.split() for r in data[:-1]]))
)

temp = i = 0
op = ops[0]
for num in zip(*data[:-1]):
    num = "".join(num)
    if not num.isspace():
        num = int(num)
        if op == "*":
            if temp:
                temp = temp * num
            else:
                temp = num
        else:
            temp += num
    else:
        i += 1
        op = ops[i]
        p2 += temp
        temp = 0
p2 += temp

print("Part 1:", p1)
print("Part 2:", p2)
