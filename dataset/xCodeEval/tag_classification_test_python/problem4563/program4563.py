    import sys
    input = input
    range = xrange
    # How to multiply matrices in 32 bit python?
    # Solution: Use doubles with homemade mult and mod.
    # This should be around 6-10 times faster than using int
    # and close to the speed you'd get in 64 bit python.
    
    MOD = 10**9 + 7
    # "Crazy code"
    MOD = 10**9 + 7
    MODF = 1.0*MOD
    MODF_inv = 1.0/MODF
    SHRT = 1.0*(1 << 16)
    SHRT_inv = 1.0/SHRT
    MAGIC = float(2**52+2**51)
    fround = lambda x:(x+MAGIC)-MAGIC
    modder = lambda a:a - MODF * fround(a*MODF_inv)
    mod_prod = lambda a, b:\
        modder(modder(a * SHRT) * fround(SHRT_inv*b) + a*(b-SHRT * fround(b*SHRT_inv)))
    
    # Quick version
    # Uses the same idea as prod but with some precalculations
def mult(A,B):
        n,m = len(A[0]),len(B)
        A = [[(Aij-SHRT*fround(Aij*SHRT_inv)) - 1j*fround(Aij*SHRT_inv) for Aij in A_j] for A_j in A]
        C = [[0.0]*n for _ in range(m)]
        for j,B_j in enumerate(B):
            C_j = C[j]
            for k,A_k in enumerate(A):
                Bkj = B_j[k] + 1j*modder(B_j[k]*SHRT)
                for i,Aik in enumerate(A_k):
                    C_j[i] += (Aik*Bkj).real
                    # Necessary for larger matrices, around 100x100:
                    #if C_j[i]>=FLOAT_PREC: C_j[i] = modder(C_j[i])
            for i in range(n):
                C_j[i] = modder(C_j[i])
        return C
    
    # Calc A^n*B
def power(A,B,n,mult_func):
        if n == 0:
            return B
        while n>5:
            if n%2==1:
                B = mult_func(A,B)
            A = mult_func(A,A)
            n//=2
        while n>1:
            B = mult_func(A,B)
            n -= 1
        return mult_func(A,B)
    
    ##### EXAMPLE
    n,m = [int(x) for x in input().split()]
    
#def DP(n):
    #    if n<=0:
    #        return 1 if n==0 else 0
    #    else:
    #        return DP(n-m) + DP(n-1)
    
    mat = [[0.0]*m for _ in range(m)]
    
    mat[0][0] = 1.0
    mat[-1][0] = 1.0
    for i in range(m-1):
        mat[i][i+1] = 1.0
    
    vec = [[1.0]*m]
    vec = power(mat,vec,n,mult)
    print(int(vec[0][-1])%MOD)