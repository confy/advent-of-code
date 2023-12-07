from collections import Counter as D
C=open('./2023/07/input.txt').readlines()
def E(h,j):
	C='J';A=D(h)
	if j:
		E=A[C];A[C]=0
		if not A:A['A']=5;B='A'
		else:B,H=A.most_common()[0];A[B]+=E
		h=h.replace(C,B)
	F={5:7,4:6,3:5 if 2 in A.values()else 4,2:3 if list(A.values()).count(2)==2 else 2,1:1};G=F[max(A.values())];return h,G
def A(l,j):
	B='J23456789TQKA'if j else'23456789TJQKA';A=[]
	for C in l:D=C[1];F,G=E(C[0],j);A.append((C[0],F,D,G))
	A.sort(key=lambda x:B.index(x[0][4]));A.sort(key=lambda x:B.index(x[0][3]));A.sort(key=lambda x:B.index(x[0][2]));A.sort(key=lambda x:B.index(x[0][1]));A.sort(key=lambda x:B.index(x[0][0]));A.sort(key=lambda x:x[3]);return sum(B[2]*(A+1)for(A,B)in enumerate(A))
B=[(A.split()[0],int(A.split()[1]))for A in C]
print(A(B,0),A(B,1))