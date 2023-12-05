J=len
I=range
N=open('./2023/05/input.txt').read()
F=N.split('\n\n')
D=[int(A)for A in F[0].split(':')[1].split()]
O,E=[[[int(A)for A in A.split()]for A in F[A].split('\n')[1:]]for A in I(1,J(F))],[(D[A],D[A+1]+D[A]-1)for A in I(0,J(D),2)]
for Z in O:
    K=[]
    for B in I(J(Z)):
        L=Z[B][1];M=Z[B][1]+Z[B][2]-1;C=[]
        for A in E:
            if M>=A[0]and L<=A[1]:
                G=max(L,A[0]);H=min(M,A[1]);K.append((G+Z[B][0]-Z[B][1],H+Z[B][0]-Z[B][1]))
                if A[0]<G:C.append((A[0],G-1))
                if A[1]>H:C.append((H+1,A[1]))
            else:C.append(A)
        E=C
    E=C+K;print(min(A[0]for A in E))