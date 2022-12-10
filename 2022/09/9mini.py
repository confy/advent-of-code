import numpy
with open('./2022/09/input.txt')as f:lines=f.readlines()
DIR_TABLE={'L':(0,-1),'R':(0,1),'U':(1,0),'D':(-1,0)}
def solve(v):
	seen={(0,0)};rope=numpy.zeros((v,2))
	for move in lines:
		d,length=move.split()
		for _ in range(int(length)):
			rope[0]+=DIR_TABLE[d]
			for i in range(1,len(rope)):
				diff=rope[i-1]-rope[i]
				if numpy.linalg.norm(diff)>=2:rope[i]+=numpy.sign(diff)
			seen.add(tuple(rope[len(rope)-1]))
	return len(seen)
print(solve(2),solve(10))