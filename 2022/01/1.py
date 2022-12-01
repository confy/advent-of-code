def read_input(filename):
    with open(filename, newline=None) as f:
        return [line.strip() for line in f.readlines()]


lines = read_input('./2022/01/input.txt')

elf_totals = []
curr_elf = 0
for line in lines:
    if line == "":
        elf_totals.append(curr_elf)
        curr_elf = 0
    else:
        curr_elf += int(line)


top_3 = sorted(elf_totals, reverse=True)[:3]

print(top_3)
print(sum(top_3))

