def inp():
        return map(int, stdin.readline().split())
    
    
def nCr(n, r):
        f, m = factorial, 1
        for i in range(n, n - r, -1):
            m *= i
        return int(m // f(r))
    
    
    from math import *
    from sys import *
    
    n, m = inp()
    if n % m == 0:
        mi = nCr(n // m, 2) * m
    else:
        mi = nCr((n // m) + 1, 2) * (n % m) + nCr(n // m, 2) * (m - (n % m))
    
    ma = nCr(n - (m - 1), 2)
    print(mi, ma)