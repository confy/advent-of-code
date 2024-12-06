L=enumerate
E=len
A=[list(A)for A in open('input.txt').read().split('\n')]
F=[-1,0,1]
G,H,M=0,0,[(A,B)for A in F for B in F if A!=0 or B!=0]
for(B,N)in L(A):
    for(C,I)in L(N):
        if I=='X':
            for(O,P)in M:
                for D in range(4):
                    J,K=C+D*O,B+D*P
                    if not(0<=J<E(A[0])and 0<=K<E(A))or A[K][J]!='XMAS'[D]:break
                    if D==3:G+=1
        if I=='A':
            if not(C+1>=E(A[0])or C-1<0 or B+1>=E(A)or B-1<0):
                if sum(1 for A in[(A[B+1][C-1],A[B-1][C+1]),(A[B+1][C+1],A[B-1][C-1])]if set(A)=={'M','S'})==2:H+=1
print(G,H)