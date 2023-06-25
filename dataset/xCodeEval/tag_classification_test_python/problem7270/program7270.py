    #!/usr/bin/python
    import sys
    from collections import defaultdict
    from itertools import combinations, combinations_with_replacement
    from fractions import Fraction as F
    # from sympy import *
    
def Ni(): return tuple(map(int, sys.stdin.readline().split()))
    
def frequency(l):
        d = defaultdict(int)
        for item in l:
            d[item] += 1
        return d
    
def factorial(k):
        r = 1
        for k in range(2, k+1):
            r = r * k
        return r
    
def choose(n, k):
        return factorial(n) / factorial(n-k) / factorial(k)
    
def d(n, m):
        a = range(n) * m
        L = []
        for c in combinations(a, n):
            L.append(tuple(sorted(frequency(c).values())))
    
        ff = frequency(L)
        # sum of ff.values() == n*m choose n
        N = choose(n*m, n)
        # print(ff)
        r = []
        for c, cf in ff.items():
            #print(c,) cf
            r.append(sum(F(_c * _c, n * n) for _c in c) * F(cf, N))
        #print(r)
        return sum(r)
    
    if False:
        r = d(2, 2)
        print(r)
        r = d(4, 4)
        print(r)
        r = d(1, 2)
        print(r)
    
def de(n, m):
        return F(1,n) + F(n - 1, n) * F(m - 1, m * n - 1) if m * n > 1 else F(1,n)
    
def fitrational(T):
        a = Symbol('a')
        b = Symbol('b')
        c = Symbol('c')
        d = Symbol('d')
        e = Symbol('e')
        f = Symbol('f')
        g = Symbol('g')
        h = Symbol('h')
        i = Symbol('i')
        j = Symbol('j')
        l = Symbol('l')
    
    def targetFunction(n, m):
            k = 1   # wlog; otherwise divide by k
            return (a * m + b * n + c * m * n + d) / \
                   (e * m * m + f * n * n + g * m * n * n + h * m * m * n + i * m * n + j * m + k * n + l)
        
        answer = targetFunction(Symbol('n'), Symbol('m'))
    
    def makeEquation(n, m, v):
            return Eq(targetFunction(n, m), v)
    
        VARS = [a,b,c,d,e,f,g,h,i,j,l]
        EQS = []
    
        # avoid n == 1 or m == 1 cases
        for n in range(2, 6):
            for m in range(2, 6):
                if len(EQS) < len(VARS):
                    EQS.append(makeEquation(n, m, T(n, m)))
    
        #for e in EQS:
        #    print(e)
        #print(len(EQS),) len(VARS)
    
        _s = solve(EQS, VARS)
        #print(_s)
    
        for var, value in _s.items():
            answer = answer.subs(var, value)
    
        return answer
        
    if False:
        for n in range(1, 6):
            for m in range(1, 6):
                print("%10s") % (d(n, m)),
            print(for) n in range(1, 6):
            for m in range(1, 6):
                print("%10s") % (de(n, m)),
            print(#) A = fitrational(d)
    # returns (-2*m*n + m + n)/(-m*n**2 + n)
    
    n, m = Ni()
def d(n, m):
        return F(-2*m*n + m + n, -m*n**2 + n) if m * n > 1 else F(1, n)
    
    print(float(d(n,) m))