# 🐇...........🐢
A=int
B=open('./2023/06/input.txt').read().strip().split('\n')
C,D=[A(B)for B in B[0].split(':')[1].split()],[A(B)for B in B[1].split(':')[1].split()]
G=list(zip(C,D))
H=A(''.join(map(str,C))),A(''.join(map(str,D)))
def E(race):A=race;return sum(1 for B in range(1,A[0])if B*(A[0]-B)>A[1])
F=1
for I in G:F*=E(I)
print(F,E(H))