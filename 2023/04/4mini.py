# 🗿
H,C,D,I,E=range,int,len,[],0
with open('./2023/04/input.txt')as L:A=L.read().strip().split('\n')
while E<D(A):
	B,M=A[E].strip().split(': ');B=B[5:];J=M.split(' | ');N={C(n)for n in J[0].split(' ')if n!=''};O={C(n)for n in J[1].split(' ')if n!=''};F=D(N.intersection(O));G=0;E+=1
	if F>0:
		G=1
		for K in H(F-1):G*=2
		I.append(G)
		for K in H(F):B=C(B);A.append(A[B+K])
print(sum(I),D(A))