F=tuple
A,C=open('input.txt').read().split('\n\n')
A=[F(map(int,A.split('-')))for A in A.splitlines()]
A.sort()
B=[]
for(D,E)in A:
	if B and B[-1][1]>=D-1:B[-1][1]=max(B[-1][1],E)
	else:B.append([D,E])
A=[F(A)for A in B]
C=[int(A)for A in C.splitlines()]
G=sum(any(A<=B<=C for(A,C)in A)for B in C)
H=sum(B-A+1 for(A,B)in A)
print(G,H)