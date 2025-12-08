H=range
B=int
P=[A.strip()for A in open('input.txt').readlines()]
I=J=0
for A in P:
	D=B(A[0]);K=0;E=0;F=len(A)
	for C in H(0,F-1):
		if B(A[C])>D:D=B(A[C]);K=C
	for L in H(K+1,F):
		if B(A[L])>E:E=B(A[L])
	I+=D*10+E;M=[];G=0
	for C in H(12):N=F-(12-C)+1;O=max(A[G:N]);Q=A.index(O,G,N);M.append(O);G=Q+1
	J+=B(''.join(M))
print(I,J)