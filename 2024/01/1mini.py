C=print
B,A=[],[]
for D in open('input.txt'):E,F=map(int,D.split());B.append(E);A.append(F)
B.sort()
A.sort()
G={r:A.count(r)for r in A}
C(sum(abs(l-r)for(l,r)in zip(B,A)))
C(sum(l*G.get(l,0)for l in B))