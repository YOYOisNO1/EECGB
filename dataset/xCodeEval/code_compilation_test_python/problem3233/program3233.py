    import sys
    from math import trunc
    # How to multiply matrices in 32 bit python?
    # Solution: Use doubles with homemade mult and mod.
    # This should be around 4-6 times faster than using int
    # and around 50% to the speed you'd get in 64 bit python.
    
    MOD = 10**9 + 7
    MODF = float(MOD)
    MODF_inv = 1.0/MODF
    FLOAT_PREC = float(2**52)
    
    # Mods float x, note modder(-1.0)=-1.0
def modder(a):
        return a - MODF * trunc(a * MODF_inv)
    
    SHRT = float(1 << 16)
    SHRT_inv = 1.0/SHRT
    # Calc modder(c+a*b)
def mod_prod(a, b, c=0):
        a1 = trunc(a*SHRT_inv)
        a2 = a-SHRT*a1
        b1 = modder(b * SHRT)
        b2 = b
        return modder(a1*b1+a2*b2+c)
    
    # Slower version, but readable
def mult(A,B):
        n,m = len(A[0]),len(B)
        C = [[0.0]*n for _ in range(m)]
        for j,B_j in enumerate(B):
            C_j = C[j]
            for k,A_k in enumerate(A):
                Bkj = B_j[k]
                for i,Aik in enumerate(A_k):
                    C_j[i] = prod(Aik,Bkj,C_j[i])
        return C
    
    # Calc A^n*B
def power(A,B,n,mult_func):
        if n == 0:
            return B
        while n>1:
            if n%2==1:
                B = mult_func(A,B)
            A = mult_func(A,A)
            n//=2
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
    print(int(vec[0][-1]))