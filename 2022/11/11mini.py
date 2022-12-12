with open('./2022/11/input.txt')as fi:monkeys_raw=fi.read().split('\n\n')
monkeys=[]
activecount={}
mod=1
items={}
def this():
	B=1
	for A in monkeys_raw:A=A.split('\n');C=int(A[0][-2]);F=[int(B)for B in A[1].split(':')[1].split(', ')];D=A[2].split(' ');G=[D[-2],D[-1]];E=int(A[3].split(' ')[-1]);B=B*E;H=int(A[4].split(' ')[-1]);I=int(A[5].split(' ')[-1]);monkeys.append([G,E,H,I]);items[C]=F;activecount[C]=0
	return B
def worry_lvl(I,o):
	if o[0]=='+':return I+int(o[1])if o[1]!='old'else I+I
	if o[0]=='*':return I*int(o[1])if o[1]!='old'else I*I
def r(p1):
	for A in items.keys():
		while items[A]:
			activecount[A]+=1;B=items[A].pop(0)
			if p1:B=worry_lvl(B,monkeys[A][0])//3
			else:B=worry_lvl(B,monkeys[A][0])%mod
			if B%monkeys[A][1]==0:items[monkeys[A][2]].append(B)
			else:items[monkeys[A][3]].append(B)
mod=this()
for i in range(20):r(True)
activity=sorted(activecount.values())
print('part1:',activity[-1]*activity[-2])
mod=this()
for i in range(10000):r(False)
activity=sorted(activecount.values())
print('part2: ',activity[-1]*activity[-2])