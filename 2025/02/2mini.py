E=range;H=len;F=G=0
for(I,J)in[tuple(map(int,A.split('-')))for A in open('input.txt').read().split(',')]:
	for C in E(I,J+1):
		D=str(C);A=H(D)
		for B in E(A//2+1,0,-1):
			if A<B*2:continue
			if D[:B]*(A//B)==D and A//B>1:
				if B==A//2 and A%2==0:F+=C
				G+=C;break
print(F,G)