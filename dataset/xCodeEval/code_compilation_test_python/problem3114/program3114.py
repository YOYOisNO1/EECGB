    from math import factorial
    from functools import partial, reduce
    from operator import mul
    from fractions import Fraction
    
    fact = [1]*101
    for i in xrange(1, 101): fact[i] = i*fact[i-1]
    
    spi = partial(reduce, mul)
def comb(a, *args):return factorial(a)/spi(factorial(x) for x in args)
    n = int(input())
    Ay = [int(i) for i in input().split()]
    Az = ([Ay[0]-1]+Ay[1:]) if Ay[0] > 0 else Ay[:]
    m = sum(Ay)
    
    if m > n: 
        print 0
        exit()
    
    Y = [[[0]*10 for j in xrange(10)] for i in xrange(n-m)]
    IY = [[[0]*10 for j in xrange(10)] for i in xrange(n-m)]
    Z = [[[0]*10 for j in xrange(10)] for i in xrange(n-m)]
    IZ = [[[0]*10 for j in xrange(10)] for i in xrange(n-m)]
    
    y = fact[m]/spi(fact[Ay[k]] for k in xrange(10))
    z = (fact[m-1]/spi(fact[Az[k]] for k in xrange(10))) if Ay[0] != 0 else 0
    
def next_table(A, X, IX, x, i, m):
        S = 0
        p = fact[m+i+1]/fact[m]
        X[i][0] = [fact[n]*fact[A[k]]/fact[A[k]+(i+1)] for k in xrange(10)]
        S += p*x*sum(X[i][0])/fact[n]
        IX[i][0] = [sum(X[i][0][k+1:]) for k in xrange(10)]
        for j in xrange(1, min(i+1, 10)):
            for k in xrange(10):
                for l in xrange(i):
                    X[i][j][k] += X[l][0][k]*IX[i-l-1][j-1][k]/fact[n]
            S += p*x*sum(X[i][j])/fact[n]
            IX[i][j] = [sum(X[i][j][k+1:]) for k in xrange(10)]
        return S
    
    S = y-z
    Sy = y
    if z:
        for i in xrange(n-m):
            Sz = next_table(Az, Z, IZ, z, i, m-1)
            Sy = next_table(Ay, Y, IY, y, i, m)
            S += Sy-Sz
    else:
        for i in xrange(n-m):
            Sz = Sy
            Sy = next_table(Ay, Y, IY, y, i, m)
            S += Sy-Sz
        
    if Ay.count(0) == 10: S-=1
    print S % 1000000007 