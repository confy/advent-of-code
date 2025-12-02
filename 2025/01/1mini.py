E=[A.strip()for A in open('input.txt').readlines()];A=50;B=0;C=0
for D in E:
	F=D[0];G=int(D[1:])
	for H in range(G):
		if F=='L':A=(A-1)%100
		else:A=(A+1)%100
		if A==0:C+=1
	if A==0:B+=1
print(B,C)