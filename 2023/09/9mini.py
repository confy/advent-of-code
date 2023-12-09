D=range
H=open('./2023/09/input.txt').read().splitlines()
E,F=0,0
for I in H:
	A=[[int(A)for A in I.split()]]
	while True:
		C=A[-1];G=[C[A+1]-C[A]for A in D(len(C)-1)];A.append(G)
		if all(A==0 for A in G):break
	A[-1].append(0);A[-1].insert(0,0)
	for B in D(len(A)-2,-1,-1):A[B].append(A[B][-1]+A[B+1][-1]);A[B].insert(0,A[B][0]-A[B+1][0])
	E+=A[0][-1];F+=A[0][0]
print(E,F)