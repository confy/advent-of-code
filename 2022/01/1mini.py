with open('./2022/01/input.txt',newline=None)as f:lines=[A.strip()for A in f.readlines()]
elf_totals=[]
curr_elf=0
for line in lines:
	if line=='':elf_totals.append(curr_elf);curr_elf=0
	else:curr_elf+=int(line)
print(sum(sorted(elf_totals,reverse=True)[:3]))