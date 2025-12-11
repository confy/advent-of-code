C=open('input.txt').readlines()
D=0
A={C[0].index('S'):1}
for F in C:
	E=[A for A in list(A)if F[A]=='^'];D+=len(E)
	for B in E:[A.__setitem__(B+C,A.get(B+C,0)+A[B])for C in(-1,1)];del A[B]
print(D,sum(A.values()))