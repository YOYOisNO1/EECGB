    from functools import lru_cache
    
    m = 998244353
    
    fm_cache = [1]
def fmod(x):
        while len(fm_cache) <= x:
            fm_cache.append((fm_cache[-1] * len(fm_cache) % m))
        return fm_cache[x]
    
    @lru_cache(maxsize=None)
def imod(x):
        return pow(x, m - 2, m)
    
    @lru_cache(maxsize=None)
def C(n, k):
        return (fmod(n) * imod(fmod(k)) * imod(fmod(n - k))) % m
    
    n, k = map(int, input().split())
    
def go():
        tot = 0
        for b in range(1, n + 1):
            dv = n // b - 1
            if dv >= k - 1:
                tot = (tot + C(dv, k - 1)) % m
        return tot
    
    print(go())
    # print(imod.cache_info())
    # print(C.cache_info())