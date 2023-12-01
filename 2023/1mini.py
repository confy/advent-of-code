with open('input.txt')as f:lines=f.readlines()
def solve(lines):
	A=None;vals=[]
	for line in lines:
		first,last=A,A
		for char in line:
			if char.isnumeric():first=char if first is A else first;last=char
		vals.append(int(first+last))
	return sum(vals)
print(solve(lines))
pairs=[('one','o1e'),('two','t2o'),('three','t3e'),('four','f4r'),('five','f5e'),('six','s6x'),('seven','s7n'),('eight','e8t'),('nine','n9e')]
new_lines=[]
for line in lines:[(line:=line.replace(w,d))for(w,d)in pairs];new_lines.append([c for c in line if c.isnumeric()])
print(solve(new_lines))
