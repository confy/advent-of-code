with open('./2022/02/input.txt')as I:J=[A.strip().split()for A in I.readlines()]
B={'X':1,'Y':2,'Z':3}
C={'A':['Y','X','Z'],'B':['Z','Y','X'],'C':['X','Z','Y']}
D=[6,3,0]
E={'X':0,'Y':3,'Z':6}
F=0
G=0
for (H,A) in J:F+=B[A]+D[C[H].index(A)];G+=E[A]+B[C[H][D.index(E[A])]]
print(F,G)