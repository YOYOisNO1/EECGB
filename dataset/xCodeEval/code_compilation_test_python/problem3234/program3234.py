    import sys
    range = xrange
    input = input
    # How to multiply matrices in 32 bit python?
    # Solution use numpy py
    
    import _numpypy
    np = _numpypy.multiarray
    
    # Windows pypy is 32 bit
    # So I'm using longlong from numpypy
    lltype = np.dtype('int64')
    llzero = lltype.type(0)
    # This is around 60 times faster than lltype.type(x) ?????!!!
def ll(x):return llzero + x
    
    MOD = ll(10**9+7)
    
def mult(A,B):
        n,m = len(A[0]),len(B)
        C = np.zeros([n,m],lltype)
        for j,B_j in enumerate(B):
            C_j = C[j]
            for k,A_k in enumerate(A):
                Bkj = B_j[k]
                for i,Aik in enumerate(A_k):
                    C_j[i] = (C_j[i]+Aik*Bkj)%MOD
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
    
    mat = np.zeros([m,m],lltype)
    
    mat[0][0] = 1
    mat[-1][0] = 1
    for i in range(m-1):
        mat[i][i+1] = 1
    
    vec = np.zeros([m,1],lltype)
    for i in range(m):vec[0][i] = 1
    
    vec = power(mat,vec,n,mult)
    print(vec[0][-1])