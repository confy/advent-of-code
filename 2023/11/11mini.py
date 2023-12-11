# 😹
from itertools import combinations as H
A,B,C=[list(A)for A in open('./2023/11/input.txt').read().split('\n')],enumerate,range
def D(g,e):
    I={A for A in C(len(g[0]))if all(g[B][A]=='.'for B in C(len(g)))};A=[];D=0
    for(J,E)in B(g):
        F=0
        for(G,K)in B(E):
            if G in I:F+=e
            if K=='#':A.append((J+D,G+F))
        if all(A=='.'for A in E):D+=e
    return sum(abs(A[0]-B[0])+abs(A[1]-B[1])for(A,B)in H(A,r=2))
print(D(A,1),D(A,999999))
