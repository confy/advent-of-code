A=sorted
B=range
with open('input.txt')as G:H=[[int(n)for n in l.split()]for l in G.readlines()]
C=lambda r:all(abs(r[i]-r[i-1])<=3>0 and r[i]!=r[i-1]for i in B(1,len(r)))and r in[A(r),A(r,reverse=1)]
I=lambda r:any(C(r[:i]+r[i+1:])for i in B(len(r)))
D=E=0
for F in H:
	if C(F):D+=1
	if I(F):E+=1
print(D,E)