D=print
with open('input.txt')as E:A=E.readlines()
def B(lines):
	C=None;D=[]
	for F in lines:
		A,E=C,C
		for B in F:
			if B.isnumeric():A=B if A is C else A;E=B
		D.append(int(A+E))
	return sum(D)
D(B(A))
F=[('one','o1e'),('two','t2o'),('three','t3e'),('four','f4r'),('five','f5e'),('six','s6x'),('seven','s7n'),('eight','e8t'),('nine','n9e')]
C=[]
for G in A:[(A:=A.replace(B,C))for(B,C)in F];C.append([A for A in G if A.isnumeric()])
D(B(C))