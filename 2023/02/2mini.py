# lol
import re
with open('input.txt')as H:I=[A.strip()for A in H.readlines()]
def A(l,c):return max(int(A.group(1))for A in re.finditer('(\\d+) '+c,l))
C,D=[],[]
for(J,B)in enumerate(I):
	E=A(B,'red');F=A(B,'green');G=A(B,'blue');D.append(E*F*G)
	if not(E>12 or F>13 or G>14):C.append(J+1)
print(sum(C),sum(D))