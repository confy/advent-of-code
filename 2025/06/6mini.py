from math import prod
F=int
G=D=0
C=open('input.txt').read()
C=C.splitlines()
E=C[-1].split()
G=sum(prod(map(F,A))if E[B]=='*'else sum(map(F,A))for(B,A)in enumerate(zip(*[A.split()for A in C[:-1]])))
A=H=0
I=E[0]
for B in zip(*C[:-1]):
	B=''.join(B)
	if not B.isspace():
		B=F(B)
		if I=='*':
			if A:A=A*B
			else:A=B
		else:A+=B
	else:H+=1;I=E[H];D+=A;A=0
D+=A
print(G,D)