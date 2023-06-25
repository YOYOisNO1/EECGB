def program4501():
    import sys
    input = sys.stdin.readline
    from math import gcd
    
    n, m = map(int, input().split())
    M = 998244353
    
    
    
    c = 0
    a = m
    b = 1
    
    for i in range(2, n+1):
        if a != 0:
            if gcd(b, i) == 1:
                b *= i
            a *= m//b
        c += pow(m, i, M) - a%M
        c %= M
    print(c)
    #kuytrfdcvbnjklkgf