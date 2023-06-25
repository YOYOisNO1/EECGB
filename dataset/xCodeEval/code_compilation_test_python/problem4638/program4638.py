    from functools import reduce
    
def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
def lcm(x, y):
        return x//gcd(x, y)*y
    
def inv(n):
        return pow(n, MOD-2, MOD)
    
def solution():
        n, a, x, y, k, M = list(map(int, input().strip().split()))
        inv_n = inv(n)
        base = reduce(lambda x, y: lcm(x, y), range(1, max(k, 2)))  # divisible by 1, 2, ..., k-1 at each round
        pr = [0]*base
        result = 0
        for i in range(n):
            pr[a%base] = (pr[a%base]+inv_n)%MOD
            result = (result + (a-a%base))%MOD  # fixed ev
            a = (a*x+y)%M
        result = (result*inv_n*k)%MOD
        for i in range(1, k+1):
            result = (result+reduce(lambda total, x: (total+x*pr[x])%MOD, range(base), 0))%MOD
            for x in range(base):
                change = pr[x]*inv_n%MOD
                pr[x] = (pr[x]-change)%MOD  # expected pr[x] after this round
                pr[x-x%i] = (pr[x-x%i]+change)%MOD  # expected pr[x-x%i] after this round
        result = (result*pow(n, k, MOD))%MOD
        return result
    
    MOD = 998244353
    print('%s' % solution())