    import sys, array, bisect, collections, heapq, itertools, math, functools
    sys.setrecursionlimit(100000)
    
def _r(): return sys.stdin.buffer.readline()
def rs(): return _r().decode('ascii').strip()
def rn(): return int(_r())
def rnt(): return tuple(map(int, _r().split()))
def rnl(): return list(rnt())
def rna(): return array.array('q', rnt())
def pnl(l): print(' '.join(map(str, l)))
    
def factorials_precalc(n, mod, inverse=True):
        fact = [1]*(n+1)
        rfact = [1]*(n+1) if inverse else None
        for i in range(1, n+1):
            fact[i] = fact[i-1] * i % mod;
            if inverse:
                rfact[i] = pow(fact[i], mod - 2, mod)
        return fact, rfact
     
    mod = 998244353
    fact, rfact = factorials_precalc(500, mod)
    
def binomial(n, k):
        return fact[n] * rfact[k] * rfact[n-k] % mod
    
    @functools.lru_cache(maxsize=None)
def solve(n, x): 
        if n == 1:
            return 0
        if x < n:
            return pow(x, n, mod)
        sol = pow(n-1, n, mod)
        for i in range(n-1):
            sol = (sol + fact[n] * rfact[i] * rfact[n-i] * pow(n-1, i, mod) * solve(n-i, x-n+1)) % mod
        return sol
     
    print(solve(*rnt()))