#🙇
I=range
C=len
from collections import defaultdict as X
D=open('./2023/10/input.txt').read().splitlines()
for A in I(C(D)):
	for B in I(C(D[A])):
		if D[A][B]=='S':F=A,B
E=X(list)
for A in I(C(D)):
	for B in I(C(D[A])):
		J=D[A][B]
		if J in'|LJ':E[A,B].append((A-1,B))
		if J in'-J7':E[A,B].append((A,B-1))
		if J in'|7F':E[A,B].append((A+1,B))
		if J in'-LF':E[A,B].append((A,B+1))
for(K,L)in[(-1,0),(0,1),(0,-1),(1,0)]:
	if F in E[F[0]+K,F[1]+L]:E[F].append((F[0]+K,F[1]+L))
G,U,P,M=F,(-1,-1),0,[]
while G!=F or not P:Y=E[G][1]if E[G][0]==U else E[G][0];U,G=G,Y;M.append(G);P+=1
Q={'|':'010010010','-':'000111000','L':'010011000','J':'010110000','7':'000110010','F':'000011010','.':'000000000'}
Q['S']=Q['J']
H=[]
for A in I(C(D)):
	H.extend(([],[],[]))
	for B in I(C(D[A])):R=[int(A)for A in Q[D[A][B]if(A,B)in M else'.']];H[-3].extend(R[:3]);H[-2].extend(R[3:6]);H[-1].extend(R[6:])
S,T,V=[(1,1)],set(),set()
while S:
	A,B=S.pop()
	if(A,B)in T:continue
	T.add((A,B));W=A//3,B//3
	if W not in M:V.add(W)
	for(K,L)in[(-1,0),(0,1),(0,-1),(1,0)]:
		N,O=A+K,B+L
		if 0<=N<C(H)and 0<=O<C(H[0])and(N,O)not in T and not H[N][O]:S.append((N,O))
print(P/2,C(D)*C(D[0])-C(M)-C(V))