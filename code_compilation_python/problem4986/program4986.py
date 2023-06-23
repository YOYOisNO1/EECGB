    import sys
    input = sys.stdin.readline
    
    from functools import lru_cache
    
    k, M = map(int, input().split())
    
    MOD = M
    
def modmul(x, y, c = 0):
        return (x * y + c) % MOD
    
    mod_mul = modmul
    
def inv(x):
        return pow(x, MOD - 2, MOD)
    
    MAX = 10 ** 6
    
    fact = [1]
    for i in range(1, MAX):
        fact.append(modmul(i, fact[i-1]))
    
    invfact = [1] * (MAX)
    invfact[MAX - 1] = inv(fact[MAX - 1])
    for i in range(MAX - 2, -1, -1):
        invfact[i] = modmul(i + 1, invfact[i+1])
    
def comb(x, y):
        assert 0 <= y <= x
        
        return modmul(fact[x], modmul(invfact[y], invfact[x - y]))
    
def invcomb(x, y):
        return modmul(invfact[x], modmul(fact[y], fact[x - y]))
    
def invs(x):
        return modmul(fact[x - 1], invfact[x])
    
    
    
    
    
    @lru_cache(maxsize = None)
def count(a, b):
        if b == 0:
            if a == 0:
                return 1
            return modmul(a, count(a - 1, 0))
    
        if a:
            o1 = modmul(a, count(a, b - 1))
        else:
            o1 = 0
    
        if b > 1:
            o2 = modmul(b - 1, count(a, b - 1))
        else:
            o2 = 0
    
    
        return (o1 + o2) % M
    
    for i in range(5000):
        for j in range(5000):
            count(i, j)
    
    n = k
    
    out = 0
    for i in range(1, n):
        for j in range(i + 1):
            if n - i - j < 0:
                continue
            
            stab = comb(n, i)
            app = modmul(comb(i, j), comb(n - i, n - i - j))
    
            order = count(j, n - i - j)
    
            u1 = pow(n - i, i - j, M)
            u2 = pow(n - 1, j, M)
    
            #print(i, j, stab, app, order, u1, u2)
            
            out += modmul(modmul(modmul(stab, app), order), modmul(u1, u2))
    
    print(out % M)
            
            