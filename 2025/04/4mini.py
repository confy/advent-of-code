J=range;D=len;A=[list(A.strip())for A in open('input.txt')];E=H=0;K=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)];F=True
while F:
	F=G=0;I=[A[:]for A in A]
	for B in J(D(A)):
		for C in J(D(A[0])):
			L=sum(A[B+E][C+F]=='@'for(E,F)in K if 0<=B+E<D(A)and 0<=C+F<D(A[0]))
			if A[B][C]=='@'and L<4:I[B][C]='.';F=1;G+=1
	A=I
	if not E:E=G
	H+=G
print(E,H)