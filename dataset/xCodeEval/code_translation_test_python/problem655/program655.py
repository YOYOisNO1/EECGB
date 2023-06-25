    import sys
    from math import trunc
    #range = xrange
    #input = input
    # How to multiply matrices in 32 bit python?
    # Solution: Use doubles with homemade mult and mod.
    
    MOD = 10**9 + 7
    MODF = float(MOD)
def modder(x):
        return x - MODF*trunc(x/MODF)
    small = 1.0 * (2**16)
    # calculates a*b+c
def prod(a,b,c):
        abig = trunc(a/small)
        return modder(abig*modder(b*small)+(a-small*abig)*b+c)
    
def mult(A,B):
        n = len(A)
        m = len(B[0])
        C = [[0.0]*n for _ in range(m)]
        
        for j,B_j in enumerate(B):
            C_j = C[j]
            for k,A_k in enumerate(A):
                Bkj = B_j[k]
                for i,Aik in enumerate(A_k):
                    C_j[i] = prod(Aik,Bkj,C_j[i])
        return C
    
def vecmult(A,B):
        n = len(A)
        C = [0.0]*n
        for k,A_k in enumerate(A):
            Bk = B[k]
            for i,Aik in enumerate(A_k):
                C[i] = prod(Aik,Bk,C[i])
        return C
    
    n,m = [int(x) for x in input().split()]
    
    
#def DP(n):
    #    if n<=0:
    #        return 1 if n==0 else 0
    #    else:
    #        return DP(n-m) + DP(n-1)
    
    
    mapper = [[0.0]*m for _ in range(m)]
    
    mapper[0][0] = 1.0
    mapper[-1][0] = 1.0
    for i in range(m-1):
        mapper[i][i+1] = 1.0
    
def power(A,B,m):
        n = len(A)
        if m == 0:
            return B
        while m>16:
            if m%2==1:
                B = vecmult(A,B)
            A = mult(A,A)
            m//=2
        while m>0:
            B = vecmult(A,B)
            m-=1
        return B
    
    vec = [1.0]*m
    vec = power(mapper,vec,n)
    print(int(vec[-1])%MOD)