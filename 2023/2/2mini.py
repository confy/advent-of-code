# lol
B,C,D,E=int,max,[],[]
import re
with open('input.txt')as I:J=[A.strip()for A in I.readlines()]
for A in J:
	K=re.search('Game (\\d+)',A).group(1);F=C([B(A.group(1))for A in re.finditer('(\\d+) red',A)]);G=C([B(A.group(1))for A in re.finditer('(\\d+) green',A)]);H=C([B(A.group(1))for A in re.finditer('(\\d+) blue',A)]);E.append(F*G*H)
	if not (F>12 or G>13 or H>14):D.append(B(K))
print(sum(D),sum(E))