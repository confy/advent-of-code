# 🎅 🤶 
C=str
from dataclasses import dataclass as E
import math
@E
class F:name:C;left:C;right:C
def D(nodes,node,condition):
	C=condition;B=nodes;A=node;D=0
	while C(A):
		for E in G:
			A=B[A.left]if E=='L'else B[A.right];D+=1
			if not C(A):break
	return D
A=[A.strip()for A in open('./2023/08/input.txt').readlines()]
G,A=A[0],A[2:]
B={A:F(A,*B[1:-1].split(', '))for(A,B)in(A.split(' = ')for A in A)}
H=D(B,B['AAA'],lambda node:node.name!='ZZZ')
I=[D(B,A,lambda node:node.name[2]!='Z')for A in B.values()if A.name[2]=='A']
print(H,math.lcm(*I))