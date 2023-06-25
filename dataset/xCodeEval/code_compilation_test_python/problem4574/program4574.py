    from fractions import gcd
    
    n = input()
    H = dict()
    inf = 10000000
    
    # m represents the minimum computed so far
def number (n,b,m):
        if not H.has_key((n,b)):
            if b == 1:                  H[n,b] = n-1
            elif n>b and b>0 and n/b<m: H[n,b] = n/b + number (b,n%b,m-n/b)
            else:                       H[n,b] = inf
        return H[n,b]
    
    m = inf
    for b in range(n+1):
        m = min (number(n,b,m),m)
    print m
    