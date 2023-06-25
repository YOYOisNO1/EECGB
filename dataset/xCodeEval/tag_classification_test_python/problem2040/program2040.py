    import functools
    
    n,k,d = map(int,input().split())
    M = 10**9+7
    
    @functools.lru_cache(maxsize=None)
def f(n,k,d) :
        if n <= 0 : return 1 if n == 0 and d == 0 else 0
        ret = 0
        for i in range(1,k+1) :
            nd = 0 if i >= d else d
            ret = (ret + f(n-i,k,nd)) % M
        return ret
    
    print(f(n,k,d))