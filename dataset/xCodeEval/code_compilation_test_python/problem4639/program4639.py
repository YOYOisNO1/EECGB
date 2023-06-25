    import sys
    from functools import reduce
    input = sys.stdin.readlines
    
def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
def lcm(x, y):
        return x//gcd(x, y)*y
    
def inv(n):
        return pow(n, MOD-2, MOD)
    
def solution():
        n, a0, x, y, k, M = list(map(int, input().strip().split()))
        a = [a0]*n
        for i in range(1, n):
            a[i] = (a[i-1]*x+y)%M
        inv_n = inv(n)
        base = reduce(lambda x, y: lcm(x, y), range(1, max(k, 2)))
        pr = [0]*base
        for x in a:
            pr[x%base] = (pr[x%base]+inv_n)%MOD
        result = ((reduce(lambda total, x: (total+(x-x%base))%MOD, a, 0)*inv_n)*k)%MOD 
        for i in range(1, k+1):
            result = (result+reduce(lambda total, x: (total+x*pr[x])%MOD, range(base), 0))%MOD
            for x in range(base):
                change = pr[x]*inv_n%MOD
                pr[x] = (pr[x]-change)%MOD
                pr[x-x%i] = (pr[x-x%i]+change)%MOD
        result = (result*pow(n, k, MOD))%MOD
        return result
        
    MOD = 998244353
    print('%s' % solution())