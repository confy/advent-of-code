# lol 🏌️ ⛳
import re
I=open('input.txt').read().splitlines()
def A(l,c):return max(int(A.group(1))for A in re.finditer('(\\d+) '+c,l))
C,D=0,0
for(J,B)in enumerate(I,1):
	E=A(B,'red');F=A(B,'green');G=A(B,'blue');D+=E*F*G
	if not(E>12 or F>13 or G>14):C+=J
print(C,D)